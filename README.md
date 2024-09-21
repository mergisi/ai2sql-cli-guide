# AI2SQL CLI User Guide

Convert natural language to SQL using AI. This guide provides installation instructions, usage examples, and best practices for MySQL, PostgreSQL, and SQLite.

For comprehensive documentation and the latest updates, visit [ai2sql.io](https://ai2sql.io).

## Installation

```bash
pip install ai2sql-cli
```

## Setup

1. Get your AI2SQL credentials:
   - Visit [ai2sql.io](https://ai2sql.io) and sign up for an account.
   - Retrieve your username and password from your account dashboard.

2. Set your AI2SQL credentials as environment variables:
   ```bash
   export AI2SQL_USERNAME=your_username
   export AI2SQL_PASSWORD=your_password
   ```

3. Get an OpenAI API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

4. Set the OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

## Basic Usage

Generate SQL:
```bash
ai2sql generate "Show all users" --dialect mysql
```

Manage connections:
```bash
ai2sql connection add --name "my_db" --dialect mysql --connection-string "mysql://user:pass@host:port/db"
ai2sql connection list
ai2sql connection remove --name "my_db"
```

Execute SQL:
```bash
ai2sql generate "Show all users" --dialect mysql --connection "my_db" --run
```

## Database-Specific Usage

### MySQL

Add a MySQL connection:
```bash
ai2sql connection add --name "mysql_db" --dialect mysql --connection-string "mysql://username:password@hostname:3306/database_name"
```

Generate MySQL-specific query:
```bash
ai2sql generate "Show users who made a purchase in the last 30 days" --dialect mysql
```

### PostgreSQL

Add a PostgreSQL connection:
```bash
ai2sql connection add --name "postgres_db" --dialect postgresql --connection-string "postgresql://username:password@hostname:5432/database_name"
```

Generate PostgreSQL-specific query:
```bash
ai2sql generate "List all tables in the current schema" --dialect postgresql
```

### SQLite

Add a SQLite connection:
```bash
ai2sql connection add --name "sqlite_db" --dialect sqlite --connection-string "sqlite:///path/to/your/database.db"
```

Generate SQLite-specific query:
```bash
ai2sql generate "Create a new table for storing user preferences" --dialect sqlite
```

## Examples

See the `examples/` directory for more detailed usage examples.

## Troubleshooting

- Ensure your AI2SQL and OpenAI API credentials are set correctly.
- Check database credentials if connections fail.
- For unexpected results, try rephrasing your query.
- SQLite: Make sure the database file path is correct and accessible.
- PostgreSQL: Verify that the specified schema exists and you have proper permissions.
- For more troubleshooting tips and FAQs, visit [ai2sql.io/support](https://ai2sql.io/support).

## Contributing

Contributions are welcome! See CONTRIBUTING.md for details.

## License

This project is licensed under the MIT License.

## Additional Resources

- Official Website: [ai2sql.io](https://ai2sql.io)

For the latest features, tutorials, and best practices, regularly check our website and documentation.
