from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.gmail_tool import GmailTool

@CrewBase
class GmailCrew():
	"""GmailCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	
	@agent
	def email_draft_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['email_draft_writer'],
			tools=[GmailTool()],
			verbose=True
		)


	@task
	def email_draft_task(self) -> Task:
		return Task(
			config=self.tasks_config['email_draft_task'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the GmailCrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
