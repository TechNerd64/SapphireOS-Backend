import scratchattach as sa
from dotenv import load_dotenv
import os

#Load .env variables
load_dotenv()
sessionID = os.getenv("sessionID")
USERNAME = os.getenv("SCRATCH_USERNAME")

session = sa.login_by_id(sessionID, username= USERNAME)
print("Logged in as " + USERNAME)

cloud = session.connect_cloud("1227635188") #Test Program, NOT SappireOS
print("Connected to cloud project: ", cloud)

value = cloud.get_var("Cloud1")


value = cloud.get_var("Cloud1")
print("Cloud1 value is: " + str(value))