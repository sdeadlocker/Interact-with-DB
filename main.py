""" 
                       Interaction with postgres database using SQLDatabaseChain:

- This script allows interaction with a PostgreSQL database using the SQLDatabaseChain class from the langchain
  library. 
- It prompts the user for input, generates a PostgreSQL query based on the input, executes the query
  on the specified database, and displays the result.
- It utilizes the OpenAI, SQLDatabase, and SQLDatabaseChain classes from the langchain library.

"""

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import environ

# Setting up env variables
env = environ.Env()
environ.Env.read_env()

# Set up the API key 
API_KEY = env('apikey')

# Configure database variables(replace them )
# db_user = "db_user"
# db_pass = "reading from env"
db_host = "db_host"
db_name = "db_name"

# Connect to the PostgreSQL database

# db = SQLDatabase.from_uri(f"postgresql+psycopg2://postgres:{db_user}:{db_pass}@{db_host}/{db_name}")
db = SQLDatabase.from_uri(f"postgresql+psycopg2://postgres:{env('dbpass')}@{db_host}/{db_name}")

# setup language model
llm = OpenAI(temperature=0, openai_api_key=API_KEY)

# Create query instruction
QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results
of the query and return the answer.Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

{question}
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

def get_prompt():
    """
    Prompt the user for input and interact with the database.
    """
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                question = QUERY.format(question=prompt)
                print(db_chain.run(question))
            except Exception as e:
                print(e)

# Call the function to start the interaction with the user
get_prompt()
