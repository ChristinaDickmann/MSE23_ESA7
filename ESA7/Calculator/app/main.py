from fastapi import FastAPI
import requests
validator_url = "http://validator:8080/"

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
              title="Das kleine 1x1",
              description="Rechnet mit Zahlen von 0 bis 10!")

@app.get("/")
def index():
    return {"Title": "Hello Docker!"}

@app.get("/add")
def add_numbers(x: float, y: float):
    response1 = requests.get(validator_url, params={"input": str(x)})
    response2 = requests.get(validator_url, params={"input": str(y)})

    if response1.status_code == 200:
        json_response = response1.json()
        bool1 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}
    
    if response2.status_code == 200:
        json_response = response2.json()
        bool2 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}

    if not bool1:
        return {"error": error_wrongInput()}
    if not bool2:
        return {"error": error_wrongInput()}
    
    return {"result": x+y}

@app.get("/subtract")
def subtract_numbers(x: float, y: float):
    response1 = requests.get(validator_url, params={"input": str(x)})
    response2 = requests.get(validator_url, params={"input": str(y)})

    if response1.status_code == 200:
        json_response = response1.json()
        bool1 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}
    
    if response2.status_code == 200:
        json_response = response2.json()
        bool2 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}

    if not bool1:
        return {"error": error_wrongInput()}
    if not bool2:
        return {"error": error_wrongInput()}
      
    return {"result": x-y}

@app.get("/multiply")
def multiply_numbers(x: float, y: float):
    response1 = requests.get(validator_url, params={"input": str(x)})
    response2 = requests.get(validator_url, params={"input": str(y)})

    if response1.status_code == 200:
        json_response = response1.json()
        bool1 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}
    
    if response2.status_code == 200:
        json_response = response2.json()
        bool2 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}

    if not bool1:
        return {"error": error_wrongInput()}
    if not bool2:
        return {"error": error_wrongInput()}
          
    return {"result": x*y}

@app.get("/divide")
def divide_numbers(x: float, y: float):
    response1 = requests.get(validator_url, params={"input": str(x)})
    response2 = requests.get(validator_url, params={"input": str(y)})

    if response1.status_code == 200:
        json_response = response1.json()
        bool1 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}
    
    if response2.status_code == 200:
        json_response = response2.json()
        bool2 = json_response.get("result")
    else:
        return {"error": "Validator can't be reached."}

    if not bool1:
        return {"error": error_wrongInput()}
    if not bool2:
        return {"error": error_wrongInput()}
    if y == 0:
        return {"error": "You can't divide by zero!"}
    
    return {"result": x/y}

def error_wrongInput():
    return "Your input is not between 0 and 10."
