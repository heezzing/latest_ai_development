import sys
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
    inputs = {
        'topic' : 'AI Agents'
    }
    LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)