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

# Custom CSS for the top navigation bar
st.markdown("""
    <style>
        /* Custom navigation bar styling */
        .navbar {
            background-color: #f1f1f1;
            padding: 10px;
            display: flex; /* Use flexbox */
            justify-content: flex-start; /* Align items to the left */
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        .nav-button {
            background-color: transparent; /* Transparent background */
            border: 2px solid #4CAF50; /* Green border */
            color: #4CAF50; /* Green text */
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s, transform 0.2s, color 0.3s;
        }
        .nav-button:hover {
            background-color: #4CAF50; /* Green background on hover */
            color: white; /* White text on hover */
        }
        .nav-button:active {
            transform: scale(0.95); /* Button press effect */
        }
        body {
            margin: 0;
            padding-top: 60px; /* Adjust based on navbar height */
        }
    </style>
    <div class="navbar">
        <span class="nav-button" onclick="window.location.href='#career-map';">Career G</span>
        <span class="nav-button" onclick="window.location.href='#pursuit-info';">Pursuit Info</span>
    </div>
""", unsafe_allow_html=True)

# Create a Streamlit app
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

# Pursuit Info Section
st.markdown("<a id='pursuit-info'></a>", unsafe_allow_html=True)
if st.sidebar.button("Pursuit Info"):
    st.title("Pursuit Information")
    st.markdown("""
        ## Welcome to the Pursuit Information Page
        Here you can find various resources and information related to your career pursuits.
        
        - **Resource 1:** Description of Resource 1.
        - **Resource 2:** Description of Resource 2.
        - **Resource 3:** Description of Resource 3.
        
        Feel free to explore and ask questions!
    """)
