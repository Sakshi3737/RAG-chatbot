from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores
import FAISS
from transformers import pipeline

embedding_model=SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

db=FAISS.load_local(
    "vector_store",
    embedding_model,
    allow_dangerous_deserialization=True
)

generator=pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def ask_question(query):

    docs=db.similarity_search(
        query,
        k=3
    )

    context=""

    citations=[]

    for doc in docs:

        context += doc.page_content + "\n"

        citations.append(
            f"{doc.metadata['source']} Page:{doc.metadata['page']}"
        )

    prompt=f"""
    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response=generator(
        prompt,
        max_length=300
    )

    answer=response[0]["generated_text"]

    return {
        "answer":answer,
        "sources":citations
    }
