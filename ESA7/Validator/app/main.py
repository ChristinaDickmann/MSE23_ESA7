from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def validate_input(input: float):
    if input > 10:
        return {"result": False}
    if input < 0:
        return {"result": False}
    
    return {"result": True}
    