import os
import chromadb
from sentence_transformers import SentenceTransformer

# -------------------------------
# Load Embedding Model
# -------------------------------

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------
# Create ChromaDB Database
# -------------------------------

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="zepto_policies"
)

# -------------------------------
# Load Documents
# -------------------------------

docs_folder = "docs"

documents = []
document_ids = []

for file in sorted(os.listdir(docs_folder)):

    if file.endswith(".txt"):

        file_path = os.path.join(docs_folder, file)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(text)
        document_ids.append(file.replace(".txt", ""))

print(f"Loaded {len(documents)} documents.")

# -------------------------------
# Generate Embeddings
# -------------------------------

print("Generating embeddings...")

embeddings = model.encode(
    documents,
    convert_to_numpy=True
).tolist()

# -------------------------------
# Store in ChromaDB
# -------------------------------

# Remove existing documents if any
existing = collection.get()

if existing["ids"]:
    collection.delete(ids=existing["ids"])

collection.add(
    ids=document_ids,
    documents=documents,
    embeddings=embeddings
)

# -------------------------------
# Verification
# -------------------------------

print("\nEmbedding completed successfully!")

print(f"Total documents stored: {collection.count()}")

print("\nStored Document IDs:")

for doc_id in document_ids:
    print(doc_id)