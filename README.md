# Minutes of Meeting CrewAI Project

## Introduction

Welcome to the Minutes of Meeting Crew project, powered by . This project sets up a multi-agent and multi-crew AI system, leveraging the powerful and flexible framework provided by crewAI. The goal is to enable agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.


## Running the Project

To initialize the crew of AI agents and begin task execution, run the following command from the root folder of the project:
Bash
python .\minutes_of_meeting\src\minutes_of_meeting\main.py
This command initializes the MinutesOfMeetingCrew and GmailCrew, assembling the agents and assigning them tasks as defined in the configuration.


## Understanding Your Crew

The Minutes of Meeting Crew consists of multiple AI agents and crews, each with unique roles, goals, and tools.

### Minutes of Meeting Crew
Agents: MoM Summarizer and MoM Writer

Tasks: Collaborate on tasks defined in config/tasks.yaml, leveraging collective skills to achieve complex objectives.

Capabilities: Defined in config/agents.yaml, outlining the capabilities and configurations of each agent.

Output: A well-structured summary of meeting minutes in text files.


### Gmail Crew

Agents: Email Draft Writer

Tasks: Create an email draft based on meeting minutes written by the previous crew agent.

Capabilities: Defined in config/agents.yaml, outlining the capabilities and configurations of the agent.


## Final Results

The project will generate the following folders and files with output in the root folder:

MarkDown

meeting_minutes

    |__action_items.txt
    |__sentiments.txt
    |__summary.txt


chunk_0.wav

chunk_1.wav

chunk_2.wav

crewai_flow.html

## Note

Removed .env, credentials.json, crewai_flow.html and EarningsCall.wav files due to Security and size issue.
