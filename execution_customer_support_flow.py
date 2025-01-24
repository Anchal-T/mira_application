from mira_sdk import MiraClient
from mira_sdk.exceptions import FlowError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Mira Client using API key from environment variables
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Define flow name (replace with your username and flow name)
flow_name = "anchal/customer-support-chatbot-flow"  # Example: "john_doe/customer-support-chatbot-flow"

# Define input data
input_data = {
    "prime_input_1": "How do I reset my password?",         # Example query
    "prime_input_2": "Optional additional parameters"      # Optional second input
}

try:
    # Execute the flow with input data
    result = client.flow.execute(flow_name, input_data)
    print("Execution result:", result)                     # Display the execution result
except FlowError as e:
    print("Execution error:", str(e))                      # Handle any errors during execution
