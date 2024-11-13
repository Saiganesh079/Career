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

# Add overlay bar at the top using HTML and CSS
st.markdown(
    """
    <style>
        .top-bar {
            position: fixed;
            top: 0;
            width: 100%;
            height: 50px;
            background-color: #4CAF50; /* Adjust color as needed */
            color: white;
            text-align: center;
            line-height: 50px;
            font-weight: bold;
            font-size: 20px;
            z-index: 1000;
        }
        .main-content {
            padding-top: 60px; /* Adjust to avoid overlap with top bar */
        }
    </style>
    <div class="top-bar">Welcome to Career Map</div>
    """, 
    unsafe_allow_html=True
)

# Apply padding to the main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Streamlit app content
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

# Close the main content div
st.markdown('</div>', unsafe_allow_html=True)
