from ollama import chat

from src.retriever import retriever
from src.prompt import PROMPT


def retrieve_context(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context, docs


def stream_answer(question):

    context, docs = retrieve_context(
        question
    )

    prompt = PROMPT.format(
        context=context,
        question=question
    )

    response = chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    return response, docs