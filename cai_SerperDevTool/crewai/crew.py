# print("This is a test script.")
from crewai import Crew, Process
from tasks import reserch_task, write_task
from agents import News_researcher,News_Writer

try:
    crew = Crew(
    agents=[News_researcher,News_Writer],
    tasks=[reserch_task, write_task],
    process= Process.sequential,
    verbose=True,
    planning=True,
    )
    result = crew.kickoff(inputs={'topic':''})
    print(result)  

except Exception as e:
    print(f"An error occurred: {e}")

