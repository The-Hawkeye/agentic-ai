import streamlit as st
import os

from ingestion.ingest_pdf import process_pdf
from tools.vector_search import search_vector
from tools.web_search import search_web
from agents.router_agent import route_query
from llm.llm import generate_answer


st.title("Agentic PDF Assistant")


if "messages" not in st.session_state:
    st.session_state.messages = []


uploaded_file = st.file_uploader("Upload PDF", type="pdf")


if uploaded_file:

    file_path = "uploaded.pdf"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    process_pdf(file_path)

    st.success("PDF indexed successfully")


question = st.chat_input("Ask a question")


if question:

    st.session_state.messages.append({"role": "user", "content": question})

    route = route_query(question)

    if route == "vector":
        context = search_vector(question)
    else:
        context = search_web(question)

    answer = generate_answer(context, question)

    st.session_state.messages.append({"role": "assistant", "content": answer})


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if st.button("New Chat"):
    st.session_state.messages = []