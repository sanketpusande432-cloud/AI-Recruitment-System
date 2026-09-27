from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from backend.rag import create_vector_store
from backend.rag import retrieve_resume_evidence
from backend.llm import llm


class ScreeningState(TypedDict):
    resume_text: str
    question: str
    evidence: str
    answer: str


def retrieve_evidence_node(state: ScreeningState):

    vector_store = create_vector_store(
        state["resume_text"]
    )

    evidence = retrieve_resume_evidence(
        vector_store,
        state["question"]
    )

    return {"evidence": evidence}


def generate_explanation_node(state: ScreeningState):

    prompt = f"""
    You are assisting a recruiter with candidate screening.

    Use only the resume evidence provided below.
    Do not make assumptions about the candidate.

    Resume Evidence:
    {state["evidence"]}

    Question:
    {state["question"]}

    Give a short explanation based on the evidence.
    """

    response = llm.invoke(prompt)

    return {"answer": response.content}


workflow = StateGraph(ScreeningState)

workflow.add_node(
    "retrieve_evidence",
    retrieve_evidence_node
)

workflow.add_node(
    "generate_explanation",
    generate_explanation_node
)

workflow.add_edge(
    START,
    "retrieve_evidence"
)

workflow.add_edge(
    "retrieve_evidence",
    "generate_explanation"
)

workflow.add_edge(
    "generate_explanation",
    END
)

screening_workflow = workflow.compile()
