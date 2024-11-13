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

# Custom CSS for the top overlay bar
st.markdown("""
    <style>
        /* Custom overlay bar styling */
        .overlay {
            background-color: #f1f1f1;
            padding: 10px;
            display: flex; /* Use flexbox */
            justify-content: center; /* Center items */
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        .button {
            background-color: #4CAF50; /* Green background */
            border: none;
            color: white; /* White text */
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 10px; /* Space between buttons */
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s, transform 0.2s;
        }
        .button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
        body {
            margin: 0;
            padding-top: 60px; /* Adjust based on overlay height */
        }
    </style>
    <div class="overlay">
        <button class="button" id="career-g" onclick="setPage('Career G')">Career G</button>
        <button class="button" id="pursuit-info" onclick="setPage('Pursuit Info')">Pursuit Info</button>
    </div>
    <script>
        function setPage(page) {
            const params = new URLSearchParams(window.location.search);
            params.set('page', page);
            window.location.search = params.toString();
        }
    </script>
""", unsafe_allow_html=True)

# Get the selected page from the URL parameters
selected_page = st.experimental_get_query_params().get('page', ['Career G'])[0]

if selected_page == "Career G":
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

elif selected_page == "Pursuit Info":
    st.title("Pursuit Information")
    st.markdown("""
        ## Welcome to the Pursuit Information Page
        Here you can find various resources and information related to your career pursuits.
        
        - **Resource 1:** Description of Resource 1.
        - **Resource 2:** Description of Resource 2.
        - **Resource 3:** Description of Resource 3.
        
        Feel free to explore and ask questions!
    """)
