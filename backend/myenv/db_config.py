import mariadb

# Create a function to establish a database connection
def create_connection():
    connection = mariadb.connect(
        host='localhost',
        user='root',  # Replace with your MariaDB username
        password='Openai2030*',  # Replace with your MariaDB password
        database='mkono_pamoja_db'  # Replace with your database name
    )
    return connection
