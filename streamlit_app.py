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

# Track which page the user is viewing
if "page" not in st.session_state:
    st.session_state.page = "home"  # Default to the home page

# Custom CSS to hide the default header and footer, and style the navigation bar
st.markdown("""
    <style>
        /* Hide the default header */
        header {
            visibility: hidden;
        }
        /* Hide the default footer */
        footer {
            visibility: hidden;
        }
        /* Custom navigation bar styling */
        .navbar {
            background-color: #f1f1f1;
            padding: 10px;
            display: flex;
            justify-content: flex-end;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        .pursuit-button {
            background-color: transparent;
            border: 2px solid #4CAF50;
            color: #4CAF50;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
        }
        .pursuit-button:hover {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    <div class="navbar">
        <!-- Placeholder for Pursuit Button -->
    </div>
""", unsafe_allow_html=True)

# Add Pursuit button in Streamlit app
if st.button("Pursuit", key="pursuit_btn"):
    st.session_state.page = "pursuit"  # Switch to Pursuit page

# Display content based on the current page
if st.session_state.page == "home":
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
        
        # Store the user and assistant messages
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Accept user input
    query = st.chat_input("What's on your mind? ")

    # Process the user input
    if query:
        process_user_input(query)

# Pursuit Page content
elif st.session_state.page == "pursuit":
    st.title("Pursuit Page")
    st.write("Welcome to the Pursuit page! Here you can add content related to career pursuits or exploration.")

    # Add a back button to return to the main page
    if st.button("Go Back"):
        st.session_state.page = "home"
