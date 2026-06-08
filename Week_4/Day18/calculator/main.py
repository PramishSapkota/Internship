from fastapi import FastAPI, HTTPException
from Week_4.Day18.calculator.routers.pydantic_class import Values
from Week_4.Day18.calculator.routers.add import router as add_router
from Week_4.Day18.calculator.routers.sub import router as sub_router
from Week_4.Day18.calculator.routers.mul import router as mul_router

# from routers.divide import router as division_router

app = FastAPI()

@app.get("/")
def homepage():
    return {"Namaste": "Sansar"}



app.include_router(add_router)
app.include_router(sub_router)
app.include_router(mul_router)
# app.include_router(division_router)





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