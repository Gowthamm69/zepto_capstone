import chromadb

from typing import TypedDict

from sentence_transformers import SentenceTransformer

from langgraph.graph import StateGraph, END

from config import COLLECTION_NAME, TOP_K
from mock_llm import generate_response


# ---------------------------------
# Embedding Model
# ---------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(COLLECTION_NAME)


# ---------------------------------
# Graph State
# ---------------------------------

class GraphState(TypedDict):
    query: str
    intent: str
    answer: dict


# ---------------------------------
# Node 1 : Intent Classification
# ---------------------------------

def classify_intent(state: GraphState):

    query = state["query"].lower()

    retrieval_keywords = [
        "delivery",
        "refund",
        "cancel",
        "return",
        "payment",
        "order",
        "wallet",
        "subscription",
        "policy"
    ]

    if any(word in query for word in retrieval_keywords):
        state["intent"] = "retrieve"

    else:
        state["intent"] = "direct"

    return state


# ---------------------------------
# Node 2 : Retrieval + Answer
# ---------------------------------

def retrieve_and_answer(state: GraphState):

    query = state["query"]

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    documents = results["documents"][0]
    sources = results["ids"][0]

    response = generate_response(
        question=query,
        retrieved_docs=documents,
        sources=sources
    )
    state["answer"] = response

    return state


# ---------------------------------
# Node 3 : Direct Answer
# ---------------------------------

def direct_answer(state: GraphState):

    state["answer"] = {
        "answer": "Hello! How can I assist you today?",
        "sources": [],
        "confidence": 1.0
    }

    return state


# ---------------------------------
# Routing Function
# ---------------------------------

def route(state: GraphState):

    if state["intent"] == "retrieve":
        return "retrieve_and_answer"

    return "direct_answer"


# ---------------------------------
# Build LangGraph
# ---------------------------------

workflow = StateGraph(GraphState)

workflow.add_node("classify_intent", classify_intent)

workflow.add_node("retrieve_and_answer", retrieve_and_answer)

workflow.add_node("direct_answer", direct_answer)

workflow.set_entry_point("classify_intent")

workflow.add_conditional_edges(
    "classify_intent",
    route,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)

workflow.add_edge("retrieve_and_answer", END)

workflow.add_edge("direct_answer", END)

app = workflow.compile()