from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tools import tool
load_dotenv()

# call gemni models

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest", 
                             verbose = True,
                             temperature= 0.5,
                             google_api_key = os.getenv("GOOGLE_API_KEY"))


# Creating a Senior resarcher agent 


News_researcher = Agent(
    role = "Senior Researcher",
    goal = "Uncover Groung Breaking technologies in {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "I am a senior researcher with a Ph.D. in AI and a background in computer science"
        "I have spent years studying the latest advancements in AI and have a deep understanding of the field."
        "I am passionate about uncovering new and innovative technologies that can be used to improve people's lives"
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = True,

)


# creating a writer agent

News_Writer = Agent(
    role = "Writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "I am a senior news writer with over a decade of experience in journalism."
        "My expertise spans across multiple topics including technology, finance, and global events."
        "I have a keen eye for detail, a deep understanding of journalistic ethics, and am driven by a passion for delivering accurate and engaging stories."
        "My years of experience allow me to craft compelling narratives while maintaining objectivity and factual accuracy."
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = False,

)