import streamlit as st
import os
import google.generativeai as genai 

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Initialize the Google API Key
os.environ['GOOGLE_API_KEY'] = st.secrets["API_Token"]

# Configure the Gemini API
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create a chatbot model
model = genai.GenerativeModel('gemini-pro')

# Define a function to generate text responses
def generate_text_response(query):
    response = model.generate_content(query)
    return response.text

# Custom CSS for styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f5;
            padding: 20px;
            border-radius: 10px;
        }
        .sidebar .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .stChatMessage.user {
            background-color: #d1e7dd;
            color: #0f5132;
        }
        .stChatMessage.assistant {
            background-color: #cfe2ff;
            color: #1c1e21;
        }
        .stChatInput {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .stButton {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation", anchor='sidebar-title')
page = st.sidebar.radio("Go to", ["Career Map", "Pursuit Info"])

# Create a Streamlit app
if page == "Career Map":
    st.title("Career Map")

    # Initialize the chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi!, I am CareerMap. What can I help you with?"}
        ]

    # Display the chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Process and store user input
    def process_user_input(query):
        # Generate a response using the Gemini API
        with st.spinner("Thinking..."):
            response = generate_text_response(query)
        
        # Display the assistant message
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Store the user message
        st.session_state.messages.append({"role": "user", "content": query})
        
        # Store the assistant message
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Accept user input
    query = st.chat_input("What's on your mind? ")

    # Process the user input
    if query:
        process_user_input(query)

elif page == "Pursuit Info":
    st.title("Pursuit Information")
    st.markdown("""
        ## Welcome to the Pursuit Information Page
        Here you can find various resources and information related to your career pursuits.
        
        - **Resource 1:** Description of Resource 1.
        - **Resource 2:** Description of Resource 2.
        - **Resource 3:** Description of Resource 3.
        
        Feel free to explore and ask questions!
    """)
