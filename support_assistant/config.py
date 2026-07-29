import os
from dotenv import load_dotenv

load_dotenv()

MOCK_LLM = os.getenv("MOCK_LLM", "1") == "1"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "llama-3.3-70b-versatile"


COLLECTION_NAME = "zepto_policies"

TOP_K = 2