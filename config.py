# app/config.py
from dotenv import load_dotenv
import os
from arango import ArangoClient

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
ARANGO_DB_URL = os.getenv("ARANGO_DB_URL")
ARANGO_DB_USERNAME = os.getenv("ARANGO_DB_USERNAME")
ARANGO_DB_PASSWORD = os.getenv("ARANGO_DB_PASSWORD")
ARANGO_DB_NAME = os.getenv("ARANGO_DB_NAME")

# Connect to ArangoDB
client = ArangoClient(hosts=ARANGO_DB_URL)

# Access the specific database
db = client.db(ARANGO_DB_NAME, username=ARANGO_DB_USERNAME, password=ARANGO_DB_PASSWORD)

# Define the verify_connection function
def verify_connection():
    if db.has_collection('students'):
        return "Connected to the database and 'students' collection exists."
    else:
        return "Connected to the database, but 'students' collection does not exist."
