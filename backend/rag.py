from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.llm import llm


def create_vector_store(resume_text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(resume_text)

    return chunks


def retrieve_resume_evidence(chunks, query):

    if not chunks:
        return ""

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        chunks + [query]
    )

    similarities = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    best_index = similarities.argmax()

    return chunks[best_index]


def generate_rag_answer(chunks, question):

    evidence = retrieve_resume_evidence(
        chunks,
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