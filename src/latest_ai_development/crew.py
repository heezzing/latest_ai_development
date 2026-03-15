from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopmentCrew():
    """LatestAiDevelopment crew"""
    
    agents : List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )
    
    @task
    def reserch_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )
    
    @task
    def reporting_task(self) -> Task:
        return Task(
            config = self.tasks_config['reporting_task'],
            output_file='output/report.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    
    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f'Before kickoff function with inputs: {inputs}')
        return inputs
    
    @after_kickoff
    def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result
    