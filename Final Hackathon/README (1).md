# 🚀 Agentic AI Feature Planner

---

## 📌 Project Title
**Agentic AI Feature Planner**

---

## 👤 Participant  
**Muhammed Riyas M**  
Intern / Cohort Trainer  

---

## 🧠 Project Overview

This project implements a **multi-agent AI workflow** using LangChain and LLMs to convert unstructured input (like user feedback, project goals, and user journeys) into **detailed, structured planning documents**.  

Designed for **product managers, UX designers, and innovation teams**, this app provides clarity from informal ideas. Each agent specializes in one part of the pipeline — from understanding context to refining the final plan — all presented within a **beautiful, tab-based UI**.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit + Custom CSS (lavender pink to purple gradient)  
- **LLM:** Google Gemini 2.0 Flash (via LangChain)  
- **Agents:** LangChain agents with custom tools and prompts  
- **RAG:** FAISS-based retrieval from PDF files  
- **UI Features:** Blurred inputs, animated icons (📘 💻 🔍), non-editable output zones  

---

## 🧩 Agent Pipeline

| Agent # | Name                    | Responsibility |
|--------:|-------------------------|----------------|
| 1️⃣     | Project Context Interpreter | Extract objectives, target audience, and outcomes |
| 2️⃣     | User Journey Analyzer       | Identify roles, intentions, and tasks |
| 3️⃣     | Task Plan Generator         | Break plans into backend, frontend, and API tasks |
| 4️⃣     | User Action Mapper          | Translate features into user-facing steps |
| 5️⃣     | Planner Refiner Agent       | Refine plan using feedback and generate change log |

---

## 🎨 UI Features

- 🎨 Gradient background (lavender-pink → purple)
- 🪄 Floating emoji icons (📘 💻 🔍 ✏ 🧠)
- 📝 Sidebar-based input section
- 🧠 Agent outputs in tabbed layout
- 🔒 Read-only outputs for clarity
- 📋 JSON → Text formatting for readable plans

---

## 🔁 Flow Summary

1. User enters **project context** and optional feedback
2. Clicks **"✨ Run Full Pipeline"**
3. All 5 LangChain agents run sequentially
4. Each result appears in its own **dedicated tab**
5. Agent 5's output is shown as a final formatted summary

---

## 🗂 Project Flow

```
[Input] ➝ [Agent 1 ➝ Agent 2 ➝ Agent 3 ➝ Agent 4 ➝ Agent 5] ➝ [Final Output]
```

---

## 📬 Contact

- 📧 Email: riyas1401@gmail.com  
- 🔗 [LinkedIn](https://linkedin.com/in/riyas-m-92975a289)  
- 🐱 [GitHub](https://github.com/MuhammedRiyas10)  

---

> “From user chaos to AI clarity — one agent at a time.” 🌟