# import the required openai modules to create Agent 
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_default_openai_api, set_tracing_disabled

# Import the dotenv and os modules to run .env file
from dotenv import load_dotenv
import os

#import asynicio to run async function
import asyncio

# load the api key that is set in .env file
load_dotenv()
gemini_api_key =os.getenv("GEMINI_API_KEY")

# Setup the provider (3rd party)
external_provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Changing the default provider (openai to gemini)
set_default_openai_client(external_provider)

# Setup api communication method 
set_default_openai_api("chat_completions")

# Turning of the tracing
set_tracing_disabled(True)

# Setup Agent(with Instructions and model) and Runner with async function 
def run_global():
    async def main():
        agent = Agent(
            name = "Mechanical Engineering Researcher",
            instructions= "Your are mechanical engineer and researcher with multiple years of experience in this domain",
            # instructions= input("Enter the Agent Instructions: "),
            model = "gemini-2.0-flash"
        )
        result = await Runner.run(
            agent,
            "I want you to do research on the mechanism of bullet trains. how do they work? " \
            "what can be improved in them and how to make the cost effective?" \
            " do explain that in detailed manner." ,   
            # input("Enter Agent prompt: ")
        )
        # print the agent output
        print(result)
        # print(type(result))

        #changing the type of communication if it is not in str format
        text_output = str(result)

        # Saved file location checking
        # print("Saving file to: ", os.getcwd())
        
        # Opens the Readme.md file and Writes the Agents Responce 
        with open(".\Readme.md","w") as file:
            file.write(text_output)
 
    asyncio.run(main())    

    