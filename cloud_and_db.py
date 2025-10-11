import scratchattach as sa
import sqlite3
from dotenv import load_dotenv
import os
import time

# Setup SQLite database
def get_db_connection():
    conn = sqlite3.connect(':memory:', check_same_thread=False)  # Use ':memory:' for an in-memory database
    return conn

def initialize_db(conn):
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    user_data TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        conn.commit()
        print("Database initialized and 'users' table is ready.")
    except Exception as e:
        print(f"Error initializing database: {e}")

# Setup Connection to SQLite database
db_conn = get_db_connection()
initialize_db(db_conn)

#Load .env variables
load_dotenv()
sessionID = os.getenv("sessionID")
USERNAME = os.getenv("SCRATCH_USERNAME")

try:
    session = sa.login_by_id(sessionID, username=USERNAME)
    print("Logged in as " + USERNAME)
    # Make sure this is the correct project ID for SapphireOS
    cloud = session.connect_cloud("1227642308")
    print("Connected to cloud project.")
except Exception as e:
    print(f"Failed to connect to Scratch: {e}")
    exit() # Exit the script if connection fails

# Cloud Request Handlers
client = cloud.requests()

@client.request
def ping():
    print("Ping request received!")
    return "Pong!  This works great!"

@client.request
def send_user_data(argument1, argument2):
    print("User data request received!")
    print("Argument 1: ", argument1)
    print("Argument 2: ", argument2)
    return f"Received arguments: {argument1}, {argument2}"

@client.request
def on_ready():
    print("Request handler is running!")

client.start(thread = True)


print("Python script is running. Press Ctrl+C to exit.")
try:
    while True:
        # This loop prevents the main script from exiting immediately.
        # The background thread handles all the cloud requests.
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
    db_conn.close()
    print("Database connection closed. Exiting.")