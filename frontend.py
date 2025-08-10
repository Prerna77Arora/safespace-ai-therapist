import streamlit as st
import requests

# ----------------- CONFIG -----------------
BACKEND_URL = "http://localhost:8000/ask"
st.set_page_config(page_title="SafeSpace – AI Mental Health Therapist", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .user-msg {
        background-color: #DCF8C6;
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 8px;
        max-width: 70%;
        word-wrap: break-word;
    }
    .assistant-msg {
        background-color: #E8EAF6;
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 8px;
        max-width: 70%;
        word-wrap: break-word;
    }
    .chat-container {
        height: 70vh;
        overflow-y: auto;
        padding-right: 15px;
    }
    .tool-badge {
        display: inline-block;
        background: #FFECB3;
        color: #795548;
        padding: 4px 8px;
        border-radius: 8px;
        font-size: 12px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE -----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------- LAYOUT -----------------
col1, col2 = st.columns([1, 3])

# Sidebar / Left Column
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4205/4205906.png", width=120)
    st.markdown("### 🧠 SafeSpace")
    st.write("Your AI Mental Health Therapist")
    st.write("I'm here to listen and help you process your thoughts.")

# Main Chat Window / Right Column
with col2:
    st.markdown("## 💬 Chat with SafeSpace")
    chat_container = st.container()
    
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="user-msg">👤 {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat input at bottom
    user_input = st.chat_input("What's on your mind today?")

    if user_input:
        # Append user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        try:
            response = requests.post(BACKEND_URL, json={"message": user_input}, timeout=30)
            response.raise_for_status()
            res_data = response.json()
            assistant_reply = res_data.get("response", "Sorry, I couldn't process that.")
            tool_info = res_data.get("tool_called")

            # Add tool badge if applicable
            if tool_info:
                assistant_reply += f'<div class="tool-badge">Tool Used: {tool_info}</div>'

            st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})

        except requests.exceptions.RequestException as e:
            st.session_state.chat_history.append(
                {"role": "assistant", "content": f"⚠️ Unable to connect: {e}"}
            )

        st.rerun()
