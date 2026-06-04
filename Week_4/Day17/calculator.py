from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def homepage():
    return {"Namaste": "Sansar"}

class Values(BaseModel):
    first : float
    second : float

@app.post("/add")
def give_values_to_add(value:Values):
    return{"Added value": value.first + value.second}

@app.get("/add")
# http://127.0.0.1:8000/add?first=0&second=0
def addition(first: float = 0, second: float = 0):
    return {"Added value": first + second    }

@app.post("/sub")
def give_values_to_subtract(value:Values):
    return{"Subtracted value": value.first - value.second}

@app.get("/sub")
def subtraction(first: float = 0, second: float = 0):
    return {
        "Subtracted value": first - second
    }

@app.post("/mul")
def give_values_to_multiply(value:Values):
    return{"Multipled value": value.first * value.second}

@app.get("/mul")
def multiply(first: float = 0, second: float = 0):
    return {
        "Multipled value": first * second
    }

@app.post("/divide")
def give_values_to_divide(value:Values):
    if value.second == 0:
        raise HTTPException(status_code= 300 , detail= "Cannot Divide By Zero")
    return{"Division value": value.first / value.second}

@app.get("/divide")
def division(first: float = 0, second: float = 1):
    if second == 0:
        raise HTTPException(status_code= 300 , detail= "Cannot Divide By Zero")
    return {
        "Division value": first - second
    }

@app.get("/square")
def sqr(num:int = 1):
    return {"Result": num**2}

@app.get("/cube")
def cube(num:int = 1):
    return {"Result": num**3}

@app.get("/power")
def pwr(base:int = 1, exp:int = 1):
    return {"Result": base**exp}