from sentence_transformers import SentenceTransformer
from endee import Endee, Precision

# 1. Connect to Endee (local, no auth)
client = Endee()

# 2. Create index (this runs only once)
client.create_index(
    name="semantic_search",
    dimension=384,
    space_type="cosine",
    precision=Precision.INT8D
)

index = client.get_index("semantic_search")

# 3. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 4. Read text data
with open("data.txt", "r") as f:
    texts = [line.strip() for line in f if line.strip()]

# 5. Create embeddings
embeddings = model.encode(texts)

# 6. Store vectors in Endee
for i, (text, vector) in enumerate(zip(texts, embeddings)):
    index.upsert([
        {
            "id": str(i),
            "vector": vector.tolist(),
            "meta": {"text": text}
        }
    ])

print("✅ Stored", len(texts), "documents in Endee")