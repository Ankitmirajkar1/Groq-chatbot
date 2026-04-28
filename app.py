import streamlit as st
from llm import get_chat_response, build_messages

st.set_page_config(page_title="Finance Chatbot", page_icon=":money_with_wings:")

st.title("Finance Chatbot :money_with_wings:")

## Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


## Sidebar (for user history)
st.sidebar.header("Chat History")

user_queries = [
    msg["content"] for msg in st.session_state.chat_history if msg["role"] == "user"
]

if user_queries:
    for i, query in enumerate(user_queries, 1):
        st.sidebar.write(f"{i}. {query}")
else:
    st.sidebar.write("No chat history available.")

## User input and process it

user_input = st.text_input("Ask me anything about finances:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        # Process the user input and get a response
        response = get_chat_response(user_input, st.session_state.chat_history)
    
    ## Store USER role
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response})

## Chat display

st.subheader("Conversation")

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.write(f"**User:** {msg['content']}")
    else:
        st.write(f"**Assistant:** {msg['content']}")