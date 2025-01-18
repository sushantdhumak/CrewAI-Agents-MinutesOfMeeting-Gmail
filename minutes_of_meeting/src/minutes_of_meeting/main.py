#!/usr/bin/env python
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from openai import OpenAI
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path

from crews.minutesofmeeting_crew.minutesofmeeting_crew import MinitesOfMeetingCrew
from crews.gmail_crew.gmail_crew import GmailCrew

import agentops
import os

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

class MinutesofMeetingState(BaseModel):
    transcript: str = ""    
    meeting_minute: str = ""


class MinutesofMeetingFlow(Flow[MinutesofMeetingState]):

    @start()
    def generate_transcript(self):
        print("Generating Transcript")

        # Get the audio file path
        directory = Path(__file__).parent
        audio_file = str(directory) + "/EarningsCall.wav"
        
        # Load the audio file
        audio = AudioSegment.from_file(audio_file, format="wav")

        # Split the audio into chunks
        chunk_length = 60 * 1000  # 10 seconds in milliseconds
        chunks = make_chunks(audio, chunk_length)
        
        # Transcribe each chunk
        full_transcript = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i}/{len(chunks)}")

            chunk.export(f"chunk_{i}.wav", format="wav")

            with open(f"chunk_{i}.wav", "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
                full_transcript += response.text + " "

        self.state.transcript = full_transcript
        print("Transcript generated", self.state.transcript)

    
    @listen(generate_transcript)
    def generate_meeting_minute(self):
        print("Generating Meeting Minute")
        self.state.meeting_minute = MinitesOfMeetingCrew().crew().kickoff(inputs={"transcript": self.state.transcript})


    @listen(generate_meeting_minute)
    def create_email_draft_MoM(self):
        print("Creating Email Draft for Minute of Meeting")
        result = GmailCrew().crew().kickoff(inputs={"body": self.state.meeting_minute})
        print("Email Draft created", result.raw)


def kickoff():
    agentops.init(os.getenv("AGENTOPS_API_KEY"), auto_start_session=False)
    session = agentops.start_session()

    minutesofmeeting_flow = MinutesofMeetingFlow()
    minutesofmeeting_flow.plot()
    minutesofmeeting_flow.kickoff()

    session.end_session()


if __name__ == "__main__":
    kickoff()
