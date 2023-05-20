""" 
                    Interaction with postgres database using SQLDatabaseToolkit:

- This script enables interaction with a PostgreSQL database using the Language Model (LLM) and SQL queries.
- It prompts the user for input, generates a PostgreSQL query based on the input, executes the queryon the 
  specified database, and displays the result.
- It utilizes the OpenAI, SQLDatabaseToolkit and create_sql_agent from langchain library for agent and chain setup.

"""
# Import libraries
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
import environ

# Load environment variables
env = environ.Env()
environ.Env.read_env()

# Set up the API key 
API_KEY = env('apikey')


# Configure database variables(replace them)

# db_user = "db_user"
# db_pass = "reading from env"
db_host = "db_host"
db_name = "db_name"

# Connect to the PostgreSQL database

# db = SQLDatabase.from_uri(f"postgresql+psycopg2://postgres:{db_user}:{db_pass}@{db_host}/{db_name}")
db = SQLDatabase.from_uri(f"postgresql+psycopg2://postgres:{env('dbpass')}@{db_host}/{db_name}")

# Set up the LLM, toolkit, and agent executor
llm = OpenAI(model_name="text-davinci-003",openai_api_key = API_KEY)

# Setup the toolkit for the SQL database
toolkit = SQLDatabaseToolkit(db=db,llm=llm)

# Create the agent executor to run SQL queries
agent_executor = create_sql_agent(llm=llm,toolkit=toolkit,verbose=True)

# Prompt the user to enter questions and interact with the database
print("Enter 'exit' to quit")
while True:
    question = input("Enter a question: ")
    if question.lower() == "exit":
        print("Exiting...")
        break
    else:
        agent_executor.run(question)


