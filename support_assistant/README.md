# Zepto Support Assistant

## Overview

The Zepto Support Assistant is a Retrieval-Augmented Generation (RAG) application developed as part of the Capstone Project. It is designed to answer customer queries by retrieving relevant information from Zepto policy documents using semantic search and generating natural language responses using the Groq LLM.

The application uses Sentence Transformers to generate embeddings, ChromaDB as the vector database, LangGraph for workflow orchestration, FastAPI for serving REST APIs, and Groq Llama 3.3 70B Versatile for response generation.

---

# Features

- Semantic search using Sentence Transformers
- ChromaDB vector database
- LangGraph workflow orchestration
- FastAPI REST API
- Groq LLM integration
- Intent classification
- Retrieval-Augmented Generation (RAG)
- JSON response using Pydantic schema
- Docker support

---

# Project Structure

```
support_assistant/
│
├── docs/
│   ├── doc_01.txt
│   ├── doc_02.txt
│   ├── doc_03.txt
│   ├── doc_04.txt
│   ├── doc_05.txt
│   ├── doc_06.txt
│   ├── doc_07.txt
│   └── doc_08.txt
│
├── chroma_db/
│
├── embeddings.py
├── graph.py
├── prompts.py
├── mock_llm.py
├── config.py
├── schemas.py
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# System Architecture

```
                User Query
                     │
                     ▼
          Intent Classification
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
Retrieve Relevant Docs      Direct Response
          │
          ▼
Sentence Transformer Embeddings
          │
          ▼
      ChromaDB Search
          │
          ▼
    Retrieved Documents
          │
          ▼
      Prompt Template
          │
          ▼
     Groq Llama 3.3 70B
          │
          ▼
      JSON Response
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| LangGraph | Workflow Management |
| ChromaDB | Vector Database |
| Sentence Transformers | Text Embeddings |
| all-MiniLM-L6-v2 | Embedding Model |
| Groq API | Large Language Model |
| Pydantic | Response Schema |
| Docker | Containerization |

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd support_assistant
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_api_key
```

Generate embeddings

```bash
python embeddings.py
```

Run the application

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## POST /ask

Request

```json
{
    "query":"What is the delivery fee?"
}
```

Returns

```json
{
    "answer":"",
    "sources":[],
    "confidence":1.0
}
```

---

# Sample Outputs

## 1. Delivery Fee

### Request

```json
{
    "query":"What is the delivery fee?"
}
```

### Response

```json
{
  "answer": "The delivery fee for orders below INR 149 is a flat INR 25. However, if your order is over INR 149, standard delivery is free. Additionally, you have the option to choose priority delivery for an extra INR 15, which reserves the next available rider slot.",
  "sources": [
    "doc_01",
    "doc_05"
  ],
  "confidence": 1
}
```

---

## 2. Refund Policy

### Request

```json
{
    "query":"What is the refund policy?"
}
```

### Response

```json
{
  "answer": "Our refund policy states that approved refunds are credited to the original payment method within 3–5 business days, or instantly to the Zepto wallet if you opt for wallet credit.",
  "sources": [
    "doc_02",
    "doc_06"
  ],
  "confidence": 1
}
```

---

## 3. Order Cancellation

### Request

```json
{
    "query":"Can I cancel my order?"
}
```

### Response

```json
{
  "answer": "You can cancel your order for free if the status is still before 'Packed', which is typically within the first 2 minutes of placing the order. If it's already packed, I'm afraid it can't be cancelled through the app. Could you please check your order status?",
  "sources": [
    "doc_05",
    "doc_06"
  ],
  "confidence": 1
}
```

---

## 4. Payment Methods

### Request

```json
{
    "query":"What payment methods are accepted?"
}
```

### Response

```json
{
  "answer": "The available information doesn't explicitly list all the accepted payment methods. However, it does mention that gift card balance can be combined with one other payment method at checkout. This implies that there are other payment methods accepted, but the specific methods are not specified.",
  "sources": [
    "doc_07",
    "doc_02"
  ],
  "confidence": 1
}
```

---

## 5. Greeting

### Request

```json
{
    "query":"Hi"
}
```

### Response

```json
{
  "answer": "Hello! How can I assist you today?",
  "sources": [],
  "confidence": 1
}
```

---

# Performance Summary

- Number of Documents Indexed : 8
- Embedding Model : all-MiniLM-L6-v2
- Vector Database : ChromaDB
- Workflow Engine : LangGraph
- API Framework : FastAPI
- Large Language Model : Groq Llama 3.3 70B Versatile
- Response Format : JSON
- Retrieval Method : Semantic Search

---

# Future Enhancements

- Conversation memory
- Multi-turn question answering
- User authentication
- Real-time document updates
- Support for multilingual queries
- Confidence score based on retrieval similarity
- Streaming responses

---

# Conclusion

The Zepto Support Assistant demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline by integrating semantic search, vector databases, workflow orchestration, and a Large Language Model. The system successfully retrieves relevant policy documents and generates accurate, context-aware responses to customer queries through a FastAPI interface. The project showcases practical implementation of modern AI technologies including Sentence Transformers, ChromaDB, LangGraph, and Groq LLM to build an efficient customer support assistant.