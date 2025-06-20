# project_context_interpreter_agent.py

import os
import dotenv
from langchain.agents import Tool, initialize_agent, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import ChatOpenAI

# ----------------- 🔐 Load API Key -----------------
dotenv.load_dotenv()
GOOGLE_API_KEY = ("AIzaSyC0wzp9B9xOdLbW9B5sfqQq3_tVng8oUB4") 

# ----------------- 🧠 Core Function -----------------

def extract_project_context(data: str) -> str:
    prompt = f"""
You are an intelligent Product Analyst Agent.

Your job is to extract clear and structured project context from the metadata and user feedback below.

🧠 Analyze and rewrite the content into a readable summary, covering:
- 🎯 Project Objectives
- 👥 Target Audience
- ✅ Expected Outcomes

📄 Input:
\"\"\"{data}\"\"\"

🎨 Format your output as:
🎯 Objectives:
- ...

👥 Target Audience:
- ...

✅ Expected Outcomes:
- ...
"""
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",
        temperature=0.4,
        google_api_key=GOOGLE_API_KEY,
        max_output_tokens=512
    )
    return llm.invoke(prompt).content

# ----------------- 🛠️ Tool Definitions -----------------

tools = [
    Tool(
        name="ProjectContextInterpreter",
        func=extract_project_context,
        description="Extracts structured objectives, target audience, and outcomes from raw project metadata and feedback."
    )
]

# ----------------- ⚙️ Initialize Agent -----------------

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.4,
    google_api_key=GOOGLE_API_KEY,
    max_output_tokens=512
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
#     Project: EcoBuddy – A sustainability assistant mobile app.

# Goal: Help urban residents reduce their carbon footprint through personalized daily tips, local recycling guides, and eco-friendly product suggestions.

# Target Users: Environment-conscious individuals living in cities, aged 20–40.

# User Feedback:
# - “I often forget to recycle properly.”
# - “Would love reminders for eco-habits.”
# - “Need an easy way to find sustainable alternatives while shopping.”

#     """

#     print("\n--- 🧠 Extracted Project Context ---")
#     print(agent_executor.run(f"Extract project context from this: {sample_input}"))
