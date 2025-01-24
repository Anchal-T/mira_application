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

test_input = {
    "customer_query": "How can I reset my password?",
    "customer_id": "CUST12345"
}

try:
    response = client.flow.test(flow, test_input)
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))
