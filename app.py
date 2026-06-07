import streamlit as st

from src.rag import stream_answer

st.set_page_config(
    page_title="eBay RAG Chatbot"
)

st.title("eBay RAG Chatbot")

question = st.chat_input(
    "Ask a question about the document"
)

if question:

    st.chat_message("user").write(
        question
    )

    response_stream, docs = stream_answer(
        question
    )

    assistant = st.chat_message(
        "assistant"
    )

    placeholder = assistant.empty()

    full_response = ""

    for chunk in response_stream:

        token = chunk["message"]["content"]

        full_response += token

        placeholder.markdown(
            full_response
        )

    st.subheader("Retrieved Sources")

    for i, doc in enumerate(docs):

        with st.expander(
            f"Source {i+1}"
        ):
            st.write(
                doc.page_content
            )