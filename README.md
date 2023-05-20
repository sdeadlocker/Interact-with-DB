# Interact-with-DB
This code allows interaction with a PostgreSQL database using the SQLDatabaseChain class from the langchain  library. It prompts the user for input, generates a PostgreSQL query based on the input, executes the query  on the specified database, and displays the result and get insights.

A. Database Setup:
- If you already have a PostgreSQL database, skip this step.
- If you don't have a PostgreSQL database:
  - 1.Run the `db.py` script provided in the project repository. This script will create the necessary tables and add some initial rows to the database. You can modify this    script to customize the database setup according to your needs.
  - 2. Alternatively, you can create the database manually using a PostgreSQL client like pgAdmin or any other app of your choice.

B. Usage:
- To interact with the application and receive results based on specific queries:
1. Update the database connection details in the configuration file (e.g., `config.py`) with your PostgreSQL database credentials.
2. Run the main script:
   ```
   python main.py
   ```
3. Follow the prompts and enter the required information to interact with the application.

- To receive general results without specific queries:
- Run the `without_query.py` script:
  ```
  python without_query.py
  ```
- This script will provide results without any specific instructions or prompts.
Below is the output:
![image (1)](https://github.com/sdeadlocker/Interact-with-DB/assets/102584952/83eff767-16fb-444f-968b-bfacda84c80f)
