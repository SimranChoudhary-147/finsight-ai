import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

DOCUMENTS_DIR = "../documents"
CHROMA_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")

def ingest_documents():
    print("📄 Loading documents...")
    loader = PyPDFDirectoryLoader(DOCUMENTS_DIR, recursive=True)
    raw_docs = loader.load()
    print(f"   Loaded {len(raw_docs)} pages")

    print("✂️  Chunking documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_documents(raw_docs)
    print(f"   Created {len(chunks)} chunks")

    print("🔢 Generating embeddings and storing in ChromaDB...")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )
    vectorstore.persist()
    print(f"✅ Done! {len(chunks)} chunks stored in ChromaDB at {CHROMA_DIR}")

def test_retrieval(query: str):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )
    results = vectorstore.similarity_search(query, k=3)
    for i, doc in enumerate(results):
        print(f"\n--- Result {i+1} ---")
        print(f"Source: {doc.metadata.get('source', 'unknown')}")
        print(f"Content: {doc.page_content[:300]}...")

if __name__ == "__main__":
    ingest_documents()  # comment to only do the testing
    test_retrieval("What is the repo rate?")