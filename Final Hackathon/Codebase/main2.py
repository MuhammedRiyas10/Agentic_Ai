import streamlit as st
import json
from Agents2.Agent1 import agent_executor as context_agent
from Agents2.Agent2 import agent_executor as journey_agent
from Agents2.Agent3 import agent_executor as task_agent
from Agents2.Agent4 import agent_executor as action_agent
from Agents2.Agent5 import agent_executor as refine_agent

# ------------------ 🎨 Custom CSS ------------------
def inject_custom_css():
    st.markdown("""
    <style>
    html, body, .stApp {
        height: 100%;
        margin: 0;
        padding: 0;
        background: linear-gradient(to bottom right, #9600FF, #AEBAF8);
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
        overflow-x: hidden;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #EEBD89, #D13ABD) !important;
        color: #ffffff;
        padding: 1.5rem;
        border-top-right-radius: 20px;
        border-bottom-right-radius: 20px;
    }

    textarea {
        border-radius: 12px !important;
        font-size: 14px !important;
        color: #000000 !important;
        background-color: rgba(255, 255, 255, 0.4) !important;
        border: 1px solid #ffffff50;
        padding: 0.8em;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        backdrop-filter: blur(3px);
    }

    textarea[disabled] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #1a1a1a !important;
        cursor: default !important;
    }

    .title-style {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffffff !important;
        margin-bottom: 1rem;
    }

    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ffffff !important;
    }

    .stButton > button {
        background: white !important;
        color: #D13ABD !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.7rem 1.4rem;
        border: none;
        box-shadow: 0 0 8px rgba(209, 58, 189, 0.3);
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        background: #f9f1ff !important;
        box-shadow: 0 0 12px rgba(209, 58, 189, 0.6);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 8px;
        border-radius: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: bold;
        padding: 6px 20px;
        color: #ffffff !important;
    }

    @keyframes floatUp {
        0% { transform: translateY(0) scale(1); opacity: 0.4; }
        100% { transform: translateY(-100vh) scale(1.5); opacity: 0; }
    }

    .animated-icon {
        position: fixed;
        font-size: 2.2rem;
        opacity: 0.08;
        animation: floatUp 25s infinite ease-in;
        z-index: -1;
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------ ✨ Floating Emojis ------------------
def animated_background():
    st.markdown("""
    <div class="animated-icon" style="top: 10%; left: 5%;">📘</div>
    <div class="animated-icon" style="top: 60%; left: 80%;">💻</div>
    <div class="animated-icon" style="top: 40%; left: 20%;">🔍</div>
    <div class="animated-icon" style="top: 80%; left: 10%;">✏️</div>
    <div class="animated-icon" style="top: 30%; left: 70%;">🧠</div>
    """, unsafe_allow_html=True)

# ------------------ 🪄 JSON → Text Formatter ------------------
def format_json_output(refined_output: str) -> str:
    try:
        parsed = json.loads(refined_output)
        refined = parsed.get("refined_plan", {})
        features = refined.get("features", [])
        tasks = refined.get("tasks", [])
        actions = refined.get("actions", [])
        changes = parsed.get("change_log", [])

        result = "✅ Refined Feature Plan\n\n"
        result += "🧹 Features:\n" + "\n".join(f"- {f}" for f in features) + "\n\n"
        result += "🧠 Tasks:\n" + "\n".join(f"- {t}" for t in tasks) + "\n\n"
        result += "🢍 User Actions:\n" + "\n".join(f"- {a}" for a in actions) + "\n\n"
        result += "📝 Change Log:\n" + "\n".join(f"- {c}" for c in changes)

        return result
    except Exception as e:
        return f"⚠️ Could not format output. Showing raw JSON.\n\n{refined_output}"

# ------------------ ⚙️ Page Setup ------------------
st.set_page_config(page_title="🧠 Feature Planner", layout="wide")
inject_custom_css()
animated_background()
st.markdown('<div class="title-style">🚀 Agentic AI Feature Planner</div>', unsafe_allow_html=True)

# ------------------ 📝 Inputs ------------------
st.sidebar.header("📅 Input Zone")
project_input = st.sidebar.text_area("Enter Project Context + Feedback")
feedback_input = st.sidebar.text_area("Mentor/Peer Feedback (optional)")

# ------------------ 🧠 Agent Tabs ------------------
tabs = st.tabs(["🧠 Main Output", "Agent 1", "Agent 2", "Agent 3", "Agent 4", "Agent 5"])
context_output = journey_output = task_output = action_output = refined_output = ""

# ------------------ 🚀 Run Pipeline ------------------
if st.sidebar.button("✨ Run Full Pipeline"):
    with st.spinner("🧠 Agent 1: Interpreting context..."):
        context_output = context_agent.run(f"Extract project context from this: {project_input}")

    with st.spinner("🛍 Agent 2: Mapping journey..."):
        journey_output = journey_agent.run(f"Analyze user journey based on this input: {context_output}\n\n{project_input}")

    with st.spinner("💠 Agent 3: Planning features & tasks..."):
        task_input = f"Project Context:\n{context_output}\n\nUser Journey Map:\n{journey_output}"
        task_output = task_agent.run(f"Generate task plan based on this: {task_input}")

    with st.spinner("👤 Agent 4: Mapping user actions..."):
        action_input = f"User Journey Map:\n{journey_output}\n\nFeature Plan:\n{task_output}"
        action_output = action_agent.run(f"Generate user actions based on this: {action_input}")

    with st.spinner("🔁 Agent 5: Refining full plan..."):
        refine_input = f"Feature Plan:\n{task_output}\n\nActions:\n{action_output}\n\nFeedback:\n{feedback_input or 'No feedback'}"
        refined_output = refine_agent.run(f"Refine the plan with this input: {refine_input}")

# ------------------ 📤 MAIN OUTPUT ------------------
with tabs[0]:
    st.subheader("📄 Final Refined Output (Formatted)")
    st.text_area("📋 Final Plan Output", refined_output, height=500, key="final_formatted", disabled=True)


# ------------------ 🧠 AGENT TABS ------------------
with tabs[1]:
    st.subheader("🧠 Agent 1: Project Context")
    st.text_area("Agent 1 Output", context_output, height=300, key="agent1_output", disabled=True)

with tabs[2]:
    st.subheader("🧭 Agent 2: User Journey Map")
    st.text_area("Agent 2 Output", journey_output, height=300, key="agent2_output", disabled=True)

with tabs[3]:
    st.subheader("🛠 Agent 3: Feature & Task Plan")
    st.text_area("Agent 3 Output", task_output, height=300, key="agent3_output", disabled=True)

with tabs[4]:
    st.subheader("👤 Agent 4: User Actions")
    st.text_area("Agent 4 Output", action_output, height=300, key="agent4_output", disabled=True)

with tabs[5]:
    st.subheader("🔁 Agent 5: Final Plan ")
    st.text_area("Agent 5 Output", refined_output, height=500, key="agent5_output", disabled=True)
