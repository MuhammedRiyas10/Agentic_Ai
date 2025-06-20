# planner_refiner_agent.py

import os
import dotenv
from langchain.agents import Tool, initialize_agent, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import ChatOpenAI
# ----------------- 🔐 Load API Key -----------------
dotenv.load_dotenv()
GOOGLE_API_KEY = ("AIzaSyBsgtO0G517iuDX4DN7DMgafjJnh2XrJxs")

# ----------------- 🧠 Planner Refinement Logic -----------------

def refine_plan_with_feedback(input_data: str) -> str:
    prompt = f"""
You are a Strategic AI Planner.

Your job is to refine a task-feature-action plan based on mentor/peer feedback, and return a developer-ready format.

📌 Responsibilities:
- Adjust or reprioritize features
- Refine or simplify user actions
- Generate a clear change log
- Output must be plain text (not JSON)

📥 Input:
\"\"\"{input_data}\"\"\"

🎯 Output Format (text only):

✅ Final Refined Plan

📌 Features:
1. ...
2. ...
3. ...

🧰 Tasks:
1. ...
2. ...
3. ...

👤 User Actions:
1. ...
2. ...
3. ...

🔄 Change Log:
- ...
- ...
- ...
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
        name="PlannerRefiner",
        func=refine_plan_with_feedback,
        description="Refine feature-task-action plan using mentor or peer feedback. Outputs updated plan + change log."
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
#     Feature Plan:
#     {{
#         "features": ["Course catalog", "Project upload", "Progress dashboard"],
#         "tasks": ["Create upload backend", "Build dashboard UI"],
#         "actions": ["User browses courses", "User uploads a project"]
#     }}

#     Feedback:
#     - "Project upload should be higher priority."
#     - "Add reminder for students to submit before deadline."
#     """

#     print("\n--- 🔁 Refined Feature Plan ---")
#     print(agent_executor.run(f"Refine the plan with this input: {sample_input}"))
