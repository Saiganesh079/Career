import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Function to render the home page
def render_home():
    st.title("Career Map")
    st.markdown("""
        <div class="navbar">
            <button onclick="document.getElementById('pursuit-section').scrollIntoView();">Pursuit</button>
        </div>
    """, unsafe_allow_html=True)

# Function to render the pursuit page
def render_pursuit():
    st.title("Pursuit")
    st.markdown("""
        <h2>Kaizen</h2>
        <p><strong>Description:</strong> Kaizen, a Japanese philosophy of continuous improvement, encourages making small, incremental changes every day to achieve larger life goals. By focusing on consistent, manageable steps, Kaizen fosters long-term progress and resilience, helping you reach your aims without overwhelming yourself. This approach is effective for both personal development and professional growth.</p>
        
        <h2>SWOT Analysis for Personal Growth</h2>
        <p><strong>Description:</strong> Common in business, SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats) can also be applied to personal development. By evaluating your internal strengths and weaknesses, as well as external opportunities and threats, you gain insights into how to maximize your potential. This structured reflection can help you make informed decisions to achieve your aims.</p>
    """)

# Navigation logic
if st.button("Pursuit"):
    st.session_state.current_page = "pursuit"

# Render the current page based on session state
if st.session_state.current_page == "home":
    render_home()
else:
    render_pursuit()
