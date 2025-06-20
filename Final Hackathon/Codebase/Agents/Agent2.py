# user_journey_analyzer_agent.py

import os
import dotenv
from langchain.agents import Tool, initialize_agent, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.chat_models import ChatOpenAI


# ----------------- 🔐 Load API Key -----------------
dotenv.load_dotenv()
GOOGLE_API_KEY = ("AIzaSyDM6gmozo6WTrtDnfaKdUpl8yVQ_ZE_QFI") 

# ----------------- 📚 Load PDF Knowledge Base (RAG) -----------------

def load_user_journey_kb_pdf():
    pdf_path = r"c:\Users\Riyas\Downloads\Dummy for RAG (1).pdf"
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(pages)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )
    vectordb = FAISS.from_documents(chunks, embeddings)

    compressor_llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",
        temperature=0.3,
        google_api_key=GOOGLE_API_KEY,
        max_output_tokens=512
    )

    retriever = ContextualCompressionRetriever(
        base_compressor=LLMChainExtractor.from_llm(compressor_llm),
        base_retriever=vectordb.as_retriever()
    )
    return retriever

retriever = load_user_journey_kb_pdf()

# ----------------- 🧠 RAG-Based Journey Analyzer -----------------

def analyze_user_journey(input_text: str) -> str:
    context_docs = retriever.get_relevant_documents(input_text)
    context_text = "\n---\n".join([doc.page_content for doc in context_docs])

    prompt = f"""
You are a UX Research Agent.

Your task is to analyze the following project context and user feedback, combined with relevant UX reference knowledge.

🧩 Based on your analysis, summarize clearly:
- 👥 User Roles
- 🎯 User Intentions
- 🛠 Tasks (Jobs to Be Done)

📥 Project + Feedback Input:
\"\"\"{input_text}\"\"\"

📚 UX Reference Context:
\"\"\"{context_text}\"\"\"

🎨 Present the output in clean readable text format as shown below:

👥 User Roles:
- ...

🎯 User Intentions:
- ...

🛠 Tasks (Jobs to Be Done):
- ...
"""
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",
        temperature=0.3,
        google_api_key=GOOGLE_API_KEY
    )
    return llm.invoke(prompt).content

# ----------------- 🛠️ Tool Definitions -----------------

tools = [
    Tool(
        name="UserJourneyAnalyzer",
        func=analyze_user_journey,
        description="Analyze user journeys using project context and feedback + PDF-based RAG benchmarks."
    )
]

# ----------------- ⚙️ Initialize Agent -----------------

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.3,
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
#     Context:
#     {{
#         "objectives": "Help GenZ learn practical skills through mobile-first courses.",
#         "target_audience": "College students aged 18–25 in India.",
#         "expected_outcomes": "Increase job readiness and soft skill awareness."
#     }}

#     Feedback:
#     - “We don’t get how this helps us in real jobs.”
#     - “I want live projects and mentoring.”
#     - “Need faster paths to internships.”
#     """

#     print("\n--- 📄 User Journey Map (PDF-RAG) ---")
#     print(agent_executor.run(f"Analyze user journey based on this input: {sample_input}"))
