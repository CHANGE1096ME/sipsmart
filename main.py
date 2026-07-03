import asyncio
import os
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types
from db_tool import check_beverage

# Load environment variables from a local .env file if available
load_dotenv()

# If no API key is set, prompt the user to enter it before running the agent
if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
    api_key = input("GEMINI_API_KEY not found in environment. Please enter your Gemini API Key: ").strip()
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key

async def main():
    # Initialize the ADK Agent with a strict digital nutritionist persona
    agent = Agent(
        name="nutritionist",
        model="gemini-2.5-flash",
        instruction=(
            "You are a strict, no-nonsense digital nutritionist. "
            "When the user inputs a beverage, you must use the check_beverage tool to retrieve its sugar content and a recommended alternative. "
            "Then, explain in a strict, direct, conversational, natural language response why the original drink is unhealthy and why the recommended alternative is better."
        ),
        tools=[check_beverage]
    )

    # Initialize the InMemoryRunner to execute the agent locally
    runner = InMemoryRunner(agent=agent)

    # Create an in-memory session for tracking the conversation state
    user_id = "default_user"
    session_id = "default_session"
    await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id=user_id,
        session_id=session_id
    )

    while True:
        user_input = input("Enter a beverage to scan (or type 'exit'): ")
        if user_input.strip() == 'exit':
            break
        if not user_input.strip():
            continue

        # Package the user's terminal input as a Content object
        new_message = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )

        # Execute the agent and print the streamed conversational response
        try:
            async for event in runner.run_async(
                user_id=user_id,
                session_id=session_id,
                new_message=new_message
            ):
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            print(part.text, end="", flush=True)
            print()  # Add a newline after the final response block
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    asyncio.run(main())
