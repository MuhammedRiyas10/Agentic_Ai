
# 🧠 Multi-Agent AI Learner

A modular, Streamlit-powered application designed to **analyze learning content from YouTube, PDFs, or text** and generate personalized learning recommendations using **multi-agent AI architecture** with LangChain + Gemini 2.0.

---

## 📌 Features

- 🎥 **YouTube Transcript Parsing**
- 📄 **PDF & Plain Text Analysis**
- 🧠 **Concept Detection**
- 👤 **Dynamic Skill Profile Updating**
- 📚 **Resource Recommendations from PDF via RAG**
- 🚀 Powered by **Gemini 2.0 Flash**, **LangChain**, and **Streamlit**

---

## 📂 Project Structure

```
MULTIAGENTSLANG/
│
├── Agents/
│   ├── input_parser.py         # Parses YouTube, PDFs, or raw text
│   ├── content_detection.py    # Detects key concepts from input
│   ├── profile.py              # Updates a skill profile JSON file
│   ├── recommender.py          # Recommends resources using PDF + RAG
│   └── user_profile.json       # Stores detected skills
│
├── data/
│   ├── learning_resources.pdf
│   └── PROMPT ENG.pdf          # Used for RAG recommendations
│
├── env/                        # Optional: your virtual environment
│
├── main.py                     # 🔥 Main Streamlit app (UI + agent flow)
├── requirements.txt            # 📦 Python dependencies
└── README.md                   # 📖 This file
```

---

## 🚀 How It Works

1. **User selects input type**: YouTube URL, PDF, or plain text.
2. **Input Parser Agent**:
   - Extracts transcript, text, or cleans pasted content.
3. **Concept Detection Agent**:
   - Detects skills or learning concepts from the input.
4. **Profile Mapping Agent**:
   - Updates a local JSON profile (`user_profile.json`) with detected skills.
5. **Recommender Agent (RAG-based)**:
   - Loads a static knowledge PDF (e.g., `PROMPT ENG.pdf`)
   - Uses LangChain + VectorStore to retrieve relevant learning materials.
   - Responds to user learning queries.

---

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/MULTIAGENTSLANG.git
cd MULTIAGENTSLANG

# 2. Create & activate virtual environment
python -m venv env
# Windows:
env\Scripts\activate
# Linux/macOS:
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run main.py
```

---

## 🧠 Agent Descriptions

| Agent Name           | Purpose                              | File                    |
|----------------------|---------------------------------------|-------------------------|
| `Input Parser`       | Extracts and cleans input content     | `input_parser.py`       |
| `Concept Detector`   | Detects concepts/skills from text     | `content_detection.py`  |
| `Profile Mapper`     | Updates skill profile (JSON)          | `profile.py`            |
| `Recommender (RAG)`  | Answers user queries using PDFs       | `recommender.py`        |

---

## 🔐 API Key Setup

Make sure your **Gemini API Key** is set in the environment or loaded securely inside your agent files.

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

## 🧪 Example Queries

- _"Recommend resources for prompt engineering"_
- _"Suggest material to learn LangChain agents"_
- _"What should I study to get better at AI pipelines?"_

---

## 📸 UI Preview

> Coming soon: screenshots of each agent output flow (Parsed Text, Concepts, Profile, RAG Results)

---

## 📌 Notes

- This system is **offline-ready** for RAG (uses static PDFs)
- All logic is modular and lives inside the `Agents/` folder
- Easy to expand with new agent types (e.g., Emotion Analyzer, Quiz Generator)

---

## 🙌 Credits

Built with ❤️ by **Riyas**  
Structured by multi-agent prompt engineering, LLMs, and design thinking.

---

## 📃 License

MIT License. Free for personal and educational use.
