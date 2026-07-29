from fastapi import FastAPI

from graph import app as graph

from schemas import QueryRequest, QueryResponse


# ---------------------------------
# FastAPI App
# ---------------------------------

app = FastAPI(
    title="Zepto Support Assistant",
    version="1.0.0"
)


# ---------------------------------
# Home Endpoint
# ---------------------------------

@app.get("/")
def home():

    return {
        "message": "Zepto Support Assistant API is running!"
    }


# ---------------------------------
# Ask Endpoint
# ---------------------------------

@app.post("/ask", response_model=QueryResponse)
def ask(request: QueryRequest):

    state = {
        "query": request.query,
        "intent": "",
        "answer": {}
    }

    result = graph.invoke(state)

    return QueryResponse(
        answer=result["answer"]["answer"],
        sources=result["answer"]["sources"],
        confidence=result["answer"]["confidence"]
    )