import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(
    page_title="PublicPrompt Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar with information
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    """
    **PublicPrompt Chatbot** helps you get information about PC&CMD Punjab.
    
    You can ask about:
    - Commodity prices (wheat, sugar, flour)
    - Complaints or feedback
    - Office timings & contacts
    - License and payment info
    - Warehouses & ration shops
    """
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Callback function to process user input
def process_input():
    user_input = st.session_state.user_input
    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Get bot response
        response = get_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": response})
        # Clear input box
        st.session_state.user_input = ""

# Title and intro
st.markdown("<h1 style='text-align: center;'>💬 PublicPrompt Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your assistant for PC&CMD queries in Punjab</p>", unsafe_allow_html=True)
st.markdown("---")

# Display sample questions
st.markdown("### 💡 Try asking things like:")
st.markdown(
"""
- Current wheat price  
- How to report overpricing  
- PC&CMD office phone  
- Office timings  
- How to get a flour license  
- Upcoming auctions or notifications  
- Warehouse stock availability  
- Payment procedure  
- Submit feedback
"""
)

# Chat input
st.text_input(
    "Type your message here and press Enter:",
    key="user_input",
    placeholder="E.g., current wheat price or office contact",
    on_change=process_input
)

# Buttons for popular sample questions
st.markdown("### Or click a sample question:")
sample_questions = [
    "Current wheat price",
    "File a complaint",
    "PC&CMD contact number",
    "Office hours",
    "Flour license procedure",
    "Upcoming auctions",
]

for q in sample_questions:
    if st.button(q):
        response = get_response(q)
        st.session_state.messages.append({"role": "user", "content": q})
        st.session_state.messages.append({"role": "bot", "content": response})

# Display chat messages (latest first)
for msg in reversed(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(
            f"<div style='background-color:#DCF8C6; color:#000; padding:10px; border-radius:15px; margin:5px 0; max-width:75%; float:right; clear:both;'>"
            f"<b>You:</b> {msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#E8E8E8; color:#000; padding:10px; border-radius:15px; margin:5px 0; max-width:75%; float:left; clear:both;'>"
            f"<b>Bot:</b> {msg['content']}</div>",
            unsafe_allow_html=True
        )

# Extra spacing at the bottom
st.markdown("<div style='margin-bottom:50px'></div>", unsafe_allow_html=True)
