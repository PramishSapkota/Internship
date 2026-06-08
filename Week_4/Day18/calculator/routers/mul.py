from fastapi import APIRouter
from Week_4.Day18.calculator.routers.pydantic_class import Values

router = APIRouter()

@router.post("/mul")
def give_values_to_multiply(value:Values):
    return{"Multipled value": value.first * value.second}

@router.get("/mul")
def multiply(first: float = 0, second: float = 0):
    return {
        "Multipled value": first * second
    }