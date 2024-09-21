from ai2sql import AI2SQL

ai2sql = AI2SQL()

# Join multiple tables
join_query = ai2sql.generate_sql("List all orders with customer names and product details", dialect="mysql")
print(f"Join Query: {join_query}")

# Aggregate data
aggregate_query = ai2sql.generate_sql("Calculate the average order value per month for the year 2023", dialect="postgresql")
print(f"Aggregate Query: {aggregate_query}")

# Subquery example
subquery = ai2sql.generate_sql("Find employees who earn more than the average salary", dialect="sqlite")
print(f"Subquery: {subquery}")
