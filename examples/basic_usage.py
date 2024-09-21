import os
from ai2sql import AI2SQL

# Ensure you've set your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

ai2sql = AI2SQL()

# Generate a simple SQL query
query = ai2sql.generate_sql("Show all users", dialect="mysql")
print(f"Generated Query: {query}")

# Generate a more complex query
complex_query = ai2sql.generate_sql("Find the top 5 customers by total purchase amount in the last month", dialect="postgresql")
print(f"Complex Query: {complex_query}")
