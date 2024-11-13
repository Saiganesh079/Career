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
            display: flex; /* Use flexbox */
            justify-content: flex-end; /* Align items to the right */
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        .pursuit-button {
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
        .pursuit-button:hover {
            background-color: #4CAF50; /* Green background on hover */
            color: white; /* White text on hover */
        }
        .pursuit-button:active {
            transform: scale(0.95); /* Button press effect */
        }
        body {
            margin: 0;
            padding-top: 60px; /* Adjust based on navbar height */
        }
    </style>
    <div class="navbar">
        <button class="pursuit-button" onclick="window.location.href='#pursuit-section';">Pursuit</button>
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

# Check which page to display
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

if st.session_state.current_page == 'home':
    st.markdown("""
        <h2>Welcome to the Career Map</h2>
        <p>Click the Pursuit button to learn more about Kaizen and SWOT Analysis.</p>
    """, unsafe_allow_html=True)

    # Pursuit button to navigate to the new page
    if st.button("Pursuit"):
        st.session_state.current_page = 'pursuit'
        st.experimental_rerun()

elif st.session_state.current_page == 'pursuit':
    st.markdown("""
        <h2>Kaizen</h2>
        <p><strong>Description:</strong> Kaizen, a Japanese philosophy of continuous improvement, encourages making small, incremental changes every day to achieve larger life goals. By focusing on consistent, manageable steps, Kaizen fosters long-term progress and resilience, helping you reach your aims without overwhelming yourself. This approach is effective for both personal development and professional growth.</p>
        
        <h2>SWOT Analysis for Personal Growth</h2>
        <p><strong>Description:</strong> Common in business, SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats) can also be applied to personal development. By evaluating your internal strengths and weaknesses, as well as external opportunities and threats, you gain insights into how to maximize your potential. This structured reflection can help you make informed decisions to achieve your aims.</p>
    """)

    # Button to go back to the home page
    if st.button("Back to Home"):
        st.session_state.current_page = 'home'
        st.experimental_rerun()
