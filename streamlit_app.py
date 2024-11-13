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
        /* Style for the top navigation bar */
        .topnav {
            background-color: #f0f2f5;
            overflow: hidden;
            border-radius: 10px;
            padding: 10px;
            display: flex;
            justify-content: center;
        }
        .topnav a {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            margin: 5px;
            text-decoration: none;
            font-size: 16px;
            transition: background-color 0.3s;
            text-align: center;
        }
        .topnav a:hover {
            background-color: #0056b3;
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

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Career Map"

# Function to switch pages
def switch_page(page_name):
    st.session_state.page = page_name

# Top navigation bar
st.markdown("""
    <div class="topnav">
        <a href="#" onclick="switch_page('Career Map')">Career Map</a>
        <a href="#" onclick="switch_page('Pursuit Info')">Pursuit Info</a>
    </div>
""", unsafe_allow_html=True)

# Page content based on the current page
if st.session_state.page == "Career Map":
    st.title("Career Map")
    st.markdown('<div id="career-map"></div>', unsafe_allow_html=True)

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

elif st.session_state.page == "Pursuit Info":
    st.title("Pursuit Information")
    st.subheader("Narrative Therapy")
    st.markdown("""
        Narrative Therapy encourages you to view life as a series of stories and to reshape the way you interpret your experiences. By reframing limiting beliefs and focusing on empowering narratives, you gain control over your life’s direction. This technique can be transformative in aligning with personal goals and creating a fulfilling life path.
    """)
    st.markdown("### Additional Resources")
    st.markdown """
        - [Narrative Therapy Overview](https://www.narrativetherapy.org)
        - [Techniques in Narrative Therapy](https://www.narrativetherapy.org/techniques)
        - [Books on Narrative Therapy](https://www.amazon.com/s?k=narrative+therapy)
    """)
