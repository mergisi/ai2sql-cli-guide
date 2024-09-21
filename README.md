# AI2SQL CLI User Guide

Convert natural language to SQL using AI. This guide provides installation instructions, usage examples, and best practices for MySQL, PostgreSQL, and SQLite.

## Installation

```bash
pip install ai2sql-cli
```

## Setup

1. Get an OpenAI API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Set the API key:
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

- Ensure your OpenAI API key is set correctly.
- Check database credentials if connections fail.
- For unexpected results, try rephrasing your query.
- SQLite: Make sure the database file path is correct and accessible.
- PostgreSQL: Verify that the specified schema exists and you have proper permissions.

## Contributing

Contributions are welcome! See CONTRIBUTING.md for details.

## License

This project is licensed under the MIT License.
