from crewai import Task
from tools import tool
from agents import News_researcher, News_Writer
reserch_task = Task(
    description = (
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and overall narrative"
        "Dollar final report should clear articulate the key points,"
        "Its marginal opportunities and potential risk"
    ),
    expected_output = 'a comprehensive three paragraph long report on the latest AI trends.',
    tools= [tool],
    agent = News_researcher,
)

write_task = Task(
    description =(
        "Compose an insightful article om {topic}."
        "Focus on the latest trends and how its impacting the industry."
        "Guess article should be easy to understand, engagingand, and positive."
    ),
    expected_output = "Of four paragraph articles on {topic} of advancement formatted as markdown.",
    tools = [tool],
    agent = News_Writer,
    async_excution = False,
    output_file = 'new_blog_post.txt',
)