import chromadb

# Initialize the ChromaDB client
client = chromadb.Client()

# Create a collection (like a table in a database)
collection = client.create_collection(name="test_collection")

# Add 3 test sentences
collection.add(
    documents=[
        "This is sentence 1 about ChromaDB.",
        "This is sentence 2 about embeddings.",
        "This is sentence 3 about vector search."
    ],
    metadatas=[
        {"source": "sentence1"},
        {"source": "sentence2"},
        {"source": "sentence3"}
    ],
    ids=["id1", "id2", "id3"]
)

# Query the collection for similar sentences
results = collection.query(
    query_texts=["What is vector search?"],
    n_results=2  # Return top 2 matches
)

# Print the results
print("Query results:")
print(results)