from fastapi import APIRouter
from Week_4.Day18.calculator.routers.pydantic_class import Values

router = APIRouter()

@router.post("/sub")
def give_values_to_subtract(value:Values):
    return{"Subtracted value": value.first - value.second}

@router.get("/sub")
def subtraction(first: float = 0, second: float = 0):
    return {
        "Subtracted value": first - second
    }