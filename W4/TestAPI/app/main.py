from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()
loud_response = []

class item(BaseModel):
    my_string = ""


# get
# 127.0.0.1:8000/
@app.get("/")
def get_root():
    """
    Get Root

    This is the root of the API.
    """
    return "Hello, World!"

# patch


# post
@app.post("/")
def post_root(my_string: str):
    """
    Post Root
    
    A simple post request endpoint, to accept a value from the client.
    """
    loud_response.append(my_string.upper())

    return json.dumps({"Greeting" : loud_response[-1]})

@app.get("/loud_response")
def get_loud_response():
    """
    Get Loud Response

    A get request to return the list of loud responses
    """
    return json.dumps({"LoudResponse": loud_response})

# put
@app.put("/loud_response/{list_index}")
def update_entry_in_response(update_string: str, list_index: str):
    """
    Update entry in loud response
    """
    loud_response[list_index] = update_string
    return json.dumps({"Entry": loud_response})

# delete
@app.delete("/loud_response")
def delete_loud_response():
    """
    Delete Loud Response list entries
    """

    loud_response.clear()
    return json.dumps({"Responses": loud_response})

# head


# options


# connect