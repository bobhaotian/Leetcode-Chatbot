from openai import OpenAI
import os

# Set the environment variable
os.environ["OPENAI_API_KEY"] = "sk-proj-uKjyAC97XmBIapJG82B0T3BlbkFJlVk68ZKEiRLjTncShWdv"

client = OpenAI()

status = client.fine_tuning.jobs.retrieve("ftjob-koxj4UoDHdlepYOtTyCMmHjs")

print(status)