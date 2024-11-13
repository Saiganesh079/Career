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

# CSS for the overlay bar
st.markdown(
    """
    <style>
    /* Overlay bar */
    .overlay-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #333;
        color: white;
        text-align: left;
        padding: 10px 20px;
        z-index: 1;
    }

    /* Button inside the overlay */
    .overlay-button {
        position: absolute;
        right: 20px;
        top: 10px;
        padding: 5px 15px;
        background-color: #4CAF50;
        border: none;
        color: white;
        cursor: pointer;
        font-size: 16px;
    }
    </style>
    <div class="overlay-bar">
        <span>Career Map</span>
        <button class="overlay-button" onclick="window.location.href='?page=2'">New Page</button>
    </div>
    """,
    unsafe_allow_html=True
)

# Page selection based on query parameter
page = st.experimental_get_query_params().get("page", ["1"])[0]

if page == "2":
    # New page content
    st.title("New Page")
    st.write("Welcome to the new page! Here you can add any additional content or functionality.")

else:
    # Default Career Map page
    st.title("Career Map")

    # Initialize the chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I am CareerMap. What can I help you with?"}
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
