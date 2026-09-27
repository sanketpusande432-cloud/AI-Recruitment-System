from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.llm import llm

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(resume_text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(resume_text)

    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store

def retrieve_resume_evidence(vector_store, query):

    documents = vector_store.similarity_search(
        query,
        k=1
    )

    if documents:
        return documents[0].page_content

    return ""

def generate_rag_answer(vector_store, question):

    evidence = retrieve_resume_evidence(
        vector_store,
        question
    )

    prompt = f"""
    You are assisting a recruiter with candidate screening.

    Use only the resume evidence provided below.
    Do not make assumptions about the candidate.

    Resume Evidence:
    {evidence}

    Question:
    {question}

    Give a short explanation based on the evidence.
    """

    response = llm.invoke(prompt)

    return response.content
