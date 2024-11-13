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

# Create a Streamlit app
st.title("Career Map")

# Custom fixed navigation bar at the top
st.markdown("""
<style>
.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: #f1f1f1;
    padding: 10px;
    text-align: center;
    z-index: 1000;
}
.nav-link {
    margin: 0 15px;
    text-decoration: none;
    color: black;
}
body {
    padding-top: 60px; /* Adjust based on header height */
}
</style>
<div class="fixed-header">
    <a class="nav-link" href="#">Home</a>
    <a class="nav-link" href="#">About</a>
    <a class="nav-link" href="#">Contact</a>
</div>
""", unsafe_allow_html=True)

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
