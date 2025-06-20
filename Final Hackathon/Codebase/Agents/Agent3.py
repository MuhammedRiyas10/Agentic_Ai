# task_plan_generator_agent.py

import os
import dotenv
from langchain.agents import Tool, initialize_agent, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import ChatOpenAI

# ----------------- 🔐 Load API Key -----------------
dotenv.load_dotenv()
GOOGLE_API_KEY = ("AIzaSyCQHeljXr58nW5nVh2QSMGs4-jlnKfGAno") 

# ----------------- 🧠 Task Plan Generator Function -----------------

def generate_task_plan(input_data: str) -> str:
    prompt = f"""
You're an AI task planner.

Given the project context below, generate a clean, human-readable plan grouped like this:

🎯 Key Features:
- Feature A
- Feature B

🛠️ Backend Tasks:
- Set up database schema
- Implement authentication

🎨 Frontend Tasks:
- Design user dashboard
- Add dark mode toggle

🔗 API Tasks:
- Connect backend to frontend
- Secure API endpoints

🧍 Linked User Outcomes:
- Users can log in and view personalized dashboard
- Real-time data sync between pages

--- CONTEXT START ---
{input_data}
--- CONTEXT END ---
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
        name="TaskPlanGenerator",
        func=generate_task_plan,
        description="Generate a structured task-feature plan including backend, frontend, and API tasks from user journeys and context."
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
#     Project Context:
#     {{
#         "objectives": "Help GenZ learn real-world skills.",
#         "target_audience": "College students aged 18–25.",
#         "expected_outcomes": "Internship readiness, hands-on skill application"
#     }}

#     User Journey Map:
#     {{
#         "user_roles": ["Student"],
#         "intentions": ["Gain practical skills", "Get job-ready"],
#         "tasks": ["Enroll in mini-courses", "Submit live project", "Track learning progress"]
#     }}
#     """

#     print("\n--- 🛠️ Feature + Task Plan ---")
#     print(agent_executor.run(f"Generate task plan based on this: {sample_input}"))
