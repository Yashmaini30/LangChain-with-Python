from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)


st.title("Ask Buddy 💬")
st.markdown("My QnA bot using langchain and google gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

history = []

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).markdown(content)
    history.append({"role": role, "content": content})

query = st.chat_input("Ask anything...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    history.append({"role": "user", "content": query})
    
    response = llm.invoke(history)
    
    st.chat_message("assistant").markdown(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})


