from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    
bob:User = {"name": "bob", "age":"20"}
#                                  ^ 
#                                  | 
#                                  | 
# mypy is giving an eror linter here but the code is working fine cuz its syntatically correct according to python
print(bob,"\n")

ram = User(name="ram", age="45")
print(type(ram))
print(ram)
print(type(ram["age"]),"\n")

#now the same thing using pydantic

from pydantic import BaseModel

class Userr(BaseModel):
    name: str
    age: int

ram = Userr(name="ram", age="30")
print(type(ram)) #"30" str is converted into int here
print(ram)
print(type(ram.age)) #"30" str is converted into int here

#"twenty" can't be converted to int so below code will throw an error
# hari = Userr(name="hari", age="twenty")
# print(hari)
# print(type(hari.age))