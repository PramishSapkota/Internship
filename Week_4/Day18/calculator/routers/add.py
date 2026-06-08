from fastapi import APIRouter
from Week_4.Day18.calculator.routers.pydantic_class import Values

router = APIRouter()

@router.post("/add")
def give_values_to_add(value:Values):
    return{"Added value": value.first + value.second}

@router.get("/add")
# http://127.0.0.1:8000/add?first=0&second=0
def addition(first: float = 0, second: float = 0):
    return {"Added value": first + second    }