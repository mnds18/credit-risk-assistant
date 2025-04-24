import os
from typing import List
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

def load_and_index_policies(policy_folder: str):
    """Loads and indexes credit policy documents."""
    texts = []
    for filename in os.listdir(policy_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(policy_folder, filename)
            print(f"Loading file: {file_path}")
            try:
                loader = TextLoader(file_path, encoding="utf-8")
                docs = loader.load()  # Returns a list of Document objects
                texts.extend([doc.page_content for doc in docs])  # Extract text content from Document objects
                print(f"Loaded {len(docs)} documents from {file_path}")  # Log number of documents loaded from each file
            except Exception as e:
                print(f"❌ Failed to load {file_path}: {e}")

    if not texts:
        raise ValueError("No valid documents found in the policy folder.")

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(docs)  # Pass Document objects to splitter

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def query_policy(vectorstore, query: str, top_k: int = 3) -> List[str]:
    """Queries the indexed policy vectorstore."""
    print(f"Querying policy with: {query}")  # Print the query being used
    try:
        results = vectorstore.similarity_search(query, k=top_k)
        print(f"Found {len(results)} results")  # Print how many results were found
    except Exception as e:
        print(f"Error during similarity search: {e}")
        return []
    
    return [doc.page_content for doc in results]


# Example usage
if __name__ == "__main__":
    store = load_and_index_policies("../documents")
    hits = query_policy(store, "What is the max DTI allowed for a home loan?")
    for i, text in enumerate(hits, 1):
        print(f"[Result {i}]:\n{text}\n")
