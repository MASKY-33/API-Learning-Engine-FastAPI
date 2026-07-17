import sqlite3

from fastapi import FastAPI



# start the backend engine to communicate with the internet
app = FastAPI()



# Lay a GET cable on the path "/" (the starting station) to the website,
# to retrieve the API data from outside (from the website) and bring it into the system to view it
@app.get("/")
def home_port():

    # Send back a simple dictionary as a welcome message
    return {"Message": "Welcome to Masky's internet engine!"}

    ## P.S.) Dictionaries (Dicts) are not databases,
    ## they are temporary Python data structures in working memory (RAM) that organize data via key-value pairs (such as a "message" and its text).
    ## The return sends this dictionary (dict) to FastAPI, which automatically converts the braces and text into a JSON package, so that your internet browser can read it.
    ## So it is just a data package, not a database.



# Lay a second, separate GET cable for the API on the path from the website to the kitchen (status_port)
@app.get("/status")
def status_port():
    
    # The API is sent empty-handed by the external website to the kitchen (status_port),
    # the API has been instructed to retrieve a data package that is already ready in the kitchen, "live status of the system", and deliver it to the external website
    return {"firewall" : "online", "database" : "connected"}



@app.post("/incident/add")
def add_incident_port(event: str):

    # The API captures the word "event" from the test website and brings it in.
    return {"Status" : "RECEIVED", "message": f"incident '{event}' successfully introduced!"}



@app.get("/incident/{incident_id}")
def get_specific_incident(incident_id: int):

    return {"message": f"De API heeft in de keuken gezocht naar {incident_id}"}

    # The number is already in the URL (/{incident_id}), where the API reads it on the journey to the kitchen,
    # The API enters the kitchen, stores the number in the function's parameter (incident_id), and the f-string pastes the number into the text {incident_id}
