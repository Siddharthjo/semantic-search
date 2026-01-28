from sentence_transformers import SentenceTransformer
from endee import Endee

# 1. Connect to Endee
client = Endee()
index = client.get_index("semantic_search")

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Take user query
query = input("Ask a question: ")

# 4. Convert query to embedding
query_vector = model.encode(query).tolist()

# 5. Search in Endee
results = index.query(
    vector=query_vector,
    top_k=3
)

# 6. Print results
print("\nTop results:\n")
for i, match in enumerate(results):
    print(f"{i+1}. {match['meta']['text']}")