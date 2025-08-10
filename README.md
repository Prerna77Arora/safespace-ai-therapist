# 🧠 SafeSpace – AI Mental Health Therapist

SafeSpace is an AI-powered mental health companion designed to provide empathetic, supportive, and resourceful conversations.  
It integrates **Streamlit** for an interactive frontend, **FastAPI** for backend processing, and multiple AI & telephony tools to assist users in mental health conversations, resource location, and crisis intervention.

---

## 🚀 Features

- 💬 **Empathetic AI Chat** powered by [MedGemma](https://ollama.ai/) and OpenAI’s GPT models.
- 📍 **Therapist Locator** to find nearby mental health professionals.
- 📞 **Emergency Call Trigger** using Twilio when crisis situations are detected.
- 🌐 **Real-Time Interaction** via a Streamlit chat interface.
- 🎨 **Custom UI Styling** for a friendly, approachable experience.

---

## 🗂 Project Structure

```
.
├── frontend.py         # Streamlit-based chat interface
├── main.py             # FastAPI backend to handle requests
├── tools.py            # AI models, Twilio API, and location tools
├── ai_agent.py         # LangChain agent with tools integration
├── config.py           # API keys and configuration
```

---

## ⚙️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **AI Models:** OpenAI GPT-4, MedGemma via [Ollama](https://ollama.ai/)  
- **Agent Framework:** [LangChain](https://www.langchain.com/)  
- **Telephony:** [Twilio API](https://www.twilio.com/)  
- **Styling:** Custom CSS in Streamlit

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/safespace.git
cd safespace
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**
```
streamlit
fastapi
uvicorn
requests
langchain
langchain_openai
langgraph
ollama
twilio
pydantic
```

### 3️⃣ Configure API Keys
Edit `config.py`:
```python
TWILIO_ACCOUNT_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_FROM_NUMBER = "+1234567890"
EMERGENCY_CONTACT = "+1987654321"
OPENAI_API_KEY = "your_openai_api_key"
```

---

## ▶️ Running the Application

### Start the Backend (FastAPI)
```bash
python main.py
```
Runs on: `http://localhost:8000`

### Start the Frontend (Streamlit)
```bash
streamlit run frontend.py
```
Runs on: `http://localhost:8501`

---

## 🛠 How It Works

1. **User Interaction** – Messages are sent from Streamlit frontend → FastAPI backend.
2. **AI Agent Processing** – Backend uses LangChain's `create_react_agent` with:
   - `ask_mental_health_specialist`
   - `find_nearby_therapists_by_location`
   - `emergency_call_tool`
3. **Tool Execution** – The correct tool is triggered depending on the conversation.
4. **Response Display** – AI or tool output is sent back to the user in the chat.

---

## ⚠️ Disclaimer
SafeSpace is **not** a substitute for professional medical advice, diagnosis, or treatment.  
In case of an emergency, contact your local helpline immediately.

---




## 👩‍💻 Author
Developed with ❤️ to promote mental well-being using AI technolog
