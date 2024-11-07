## https://serper.dev/

from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()
import os



os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
tool = SerperDevTool() 

