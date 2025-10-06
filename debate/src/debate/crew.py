from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, llm
import os
from dotenv import load_dotenv

load_dotenv(override=True)

@CrewBase
class Debate():
    """Debate crew"""


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @llm
    def proponent_llm(self):
        return LLM(
            #model="openai/gpt-5-nano",
            model="gemini/gemini-2.0-flash",
            #temperature=0.7,
            drop_params=True,
            additional_drop_params=["stop"]
        )

    @llm
    def opponent_llm(self):
        return LLM(
            #model="gemini/gemini-2.0-flash",
            model="openai/gpt-5-nano",
            #temperature=0.7,
            drop_params=True,
            additional_drop_params=["stop"]
        )
    
    @llm
    def judge_llm(self):
        return LLM(
            model="azure/Phi-4-reasoning",
            api_key=os.getenv("AZURE_API_KEY"),
            api_base=os.getenv("AZURE_API_BASE"),
            api_version=os.getenv("AZURE_API_VERSION"),
            temperature=0.7,
            drop_params=True,
            additional_drop_params=["stop"]

        )
        

    @agent
    def proponent(self) -> Agent:
        return Agent(
            config=self.agents_config['proponent'],
            verbose=True
        )
    
    @agent
    def opponent(self) -> Agent:
        return Agent(
            config=self.agents_config['opponent'],
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'],
            verbose=True
        )

    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'],
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'],
        )

    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
