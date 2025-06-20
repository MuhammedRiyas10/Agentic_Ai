# user_action_mapper_agent.py

import os
import dotenv
from langchain.agents import Tool, initialize_agent, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import ChatOpenAI

# ----------------- 🔐 Load API Key -----------------
dotenv.load_dotenv()
GOOGLE_API_KEY = ("AIzaSyCQHeljXr58nW5nVh2QSMGs4-jlnKfGAno")

# ----------------- 🧠 Action Mapping Logic -----------------

def generate_user_actions(input_data: str) -> str:
    prompt = f"""
You are a UX-focused AI Agent.

Your job is to convert feature plans and user journeys into simple, inclusive, and real-world user actions.

🧠 Guidelines:
- Avoid technical terms.
- Use clear, everyday phrases.
- Keep it concise and user-friendly.
- Write as if explaining what the user **actually does**.

📥 Input:
\"\"\"{input_data}\"\"\"

🎯 Output Format (text only):
🛠️ User Actions:

1. ...
2. ...
3. ...
    """
    llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY,
    max_output_tokens=250
)
    return llm.invoke(prompt).content
  

# ----------------- 🛠️ Tool Definitions -----------------

tools = [
    Tool(
        name="UserActionMapper",
        func=generate_user_actions,
        description="Generate contextual user actions based on feature plans and user journeys."
    )
]

# ----------------- ⚙️ Initialize Agent -----------------

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY,
    max_output_tokens=250
)


agent_executor: AgentExecutor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ----------------- 🧪 Test Run -----------------

# if __name__ == "__main__":
#     sample_input = """
#     User Journey Map:
#     {{
#         "user_roles": ["Student"],
#         "intentions": ["Gain skills", "Get mentorship"],
#         "tasks": ["Join course", "Complete project", "Track progress"]
#     }}

#     Feature Plan:
#     {{
#         "features": ["Course catalog", "Project upload", "Progress dashboard"],
#         "backend_tasks": [...],
#         "frontend_tasks": [...],
#         "api_tasks": [...],
#         "linked_user_outcomes": ["Career readiness", "Project completion"]
#     }}
#     """

#     print("\n--- ✨ User Action List ---")
#     print(agent_executor.run(f"Generate user actions based on this: {sample_input}"))
