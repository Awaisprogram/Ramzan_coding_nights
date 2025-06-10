import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

# Create an greeting agent with instructions, and model
agent = Agent(
    name="Greeting Agent",
    instructions="Help the user with their questions",
    model=model,
)

# Get user input from the terminal
while True:
    user_question = input("Please enter your question: ")
    result = Runner.run_sync(agent, user_question)
    print(result.final_output)
    if user_question.lower() == "exit":
        break


