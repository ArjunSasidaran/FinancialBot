import streamlit as st
from utils import write_message
from agent import generate_response

# Page Config
st.set_page_config("FinancialBot", page_icon=":bar_chart:")
st.title("FinancialBot")

# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm a Financial Expert specialized in answering questions from companies' 10-K forms! How can I assist you today?"},
    ]

# Submit handler
def handle_submit(message):

    # Handle the response
    with st.spinner('Thinking...'):
        # Call the agent
        response = generate_response(message)
        write_message('assistant', response)
        
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)
