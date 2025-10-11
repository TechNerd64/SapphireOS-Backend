import scratchattach as sa
from dotenv import load_dotenv
import os

#Load .env variables
load_dotenv()
sessionID = os.getenv("sessionID")
USERNAME = os.getenv("SCRATCH_USERNAME")

session = sa.login_by_id(sessionID, username= USERNAME)
print("Logged in as " + USERNAME)
cloud = session.connect_cloud("1227642308") #Test Program, NOT SappireOS
print("Connected to cloud project: ", cloud)
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