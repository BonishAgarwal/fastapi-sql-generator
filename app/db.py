import psycopg2

# Connect to PostgreSQL
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="radamatic_db",
        user="postgres",
        password="postgres"
    )