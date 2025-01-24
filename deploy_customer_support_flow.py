import os
from dotenv import load_dotenv
from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv("MIRA_API_KEY")

# Initialize Mira Client with API key
client = MiraClient(config={"API_KEY": API_KEY})
flow = CompoundFlow(source="customer_support_chatbot_flow.yaml")

try:
    client.flow.deploy(flow)
    print("Customer Support Chatbot Flow deployed successfully!")
except FlowError as e:
    print(f"Deployment error: {str(e)}")
