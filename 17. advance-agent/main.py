import os  # For accessing environment variables
import chainlit as cl  # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict  # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
import requests

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

@function_tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        result = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}"
        )
        data = result.json()
        return f"The current weather in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
    except Exception as e:
        return f"Could not fetch weather data due to: {str(e)}"


agent = Agent(
    name="Greeting Agent",
    instructions="""You are an agent that work for only weather

Your responsibilities:
 You tell the weather of city for user asked
Always maintain a friendly, professional tone and ensure responses are helpful within your defined scope.""",
    model=model,
    tools=[get_weather],
)


# Decorator to handle OAuth callback from GitHub
@cl.oauth_callback
def oauth_callback(
    provider_id: str,  # ID of the OAuth provider (GitHub)
    token: str,  # OAuth access token
    raw_user_data: Dict[str, str],  # User data from GitHub
    default_user: cl.User,  # Default user object from Chainlit
) -> Optional[cl.User]:  # Return User object or None
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")  # Print provider ID for debugging
    print(f"User data: {raw_user_data}")  # Print user data for debugging

    return default_user  # Return the default user object


# Handler for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()  # Send welcome message


# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")  # Get chat history from session

    history.append(
        {"role": "user", "content": message.content}
    )  # Add user message to history

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)
