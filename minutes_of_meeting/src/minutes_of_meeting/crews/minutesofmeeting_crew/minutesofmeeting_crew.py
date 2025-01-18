from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

file_writer_tool_summary = FileWriterTool(file_name="meeting_summary.txt", directory="minutes_of_meeting")
file_writer_tool_actions = FileWriterTool(file_name="action_items.txt", directory="minutes_of_meeting")
file_writer_tool_sentiment = FileWriterTool(file_name="sentiment.txt", directory="minutes_of_meeting")

@CrewBase
class MinitesOfMeetingCrew:
    """Minutes of Meeting Crew"""
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @agent
    def meeting_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["meeting_summarizer"],
            tools=[file_writer_tool_summary, file_writer_tool_actions, file_writer_tool_sentiment],
        )
    
    @agent
    def meeting_minutes_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["meeting_minutes_writer"],
        )

    @task
    def write_meeting_summary(self) -> Task:
        return Task(
            config=self.tasks_config["write_meeting_summary"],
        )
    
    @task
    def write_minutes_of_meeting(self) -> Task:
        return Task(
            config=self.tasks_config["write_minutes_of_meeting"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Crew for Minutes of Meeting"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
