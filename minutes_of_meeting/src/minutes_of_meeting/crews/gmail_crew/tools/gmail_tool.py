from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from .gmail_util import authenticate_gmail, create_message, create_draft
from agentops import record_tool

class GmailToolInput(BaseModel):
    """Input schema for GmailTool."""

    body: str = Field(..., description="The body of the email to send.")


@record_tool("GmailTool")
class GmailTool(BaseTool):
    name: str = "GmailTool"
    description: str = (
        "This tool is used to send emails using the Gmail API."
    )
    args_schema: Type[BaseModel] = GmailToolInput

    def _run(self, body: str) -> str:

        try:    
            service = authenticate_gmail()
            sender = "dhumaksushant@gmail.com"
            to = "someone@yahoo.co.in"
            subject = "Minutes of Meeting"
            message_text = body

            message = create_message(sender, to, subject, message_text)
            draft = create_draft(service, "me", message)

            return "Email draft created successfully!"
        except Exception as error:
            print(f'An error occurred: {error}')
    