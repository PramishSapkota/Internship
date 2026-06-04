from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Predicting student result",
    description="Dictionary stores pydantic objects",
    version="1",)

database = {}

class StudentRecord(BaseModel):
    id:int = 0
    name:str = "Ram"
    daily_study_hour:int = 8
    attendance_percent:float = 75
    previous_marks: float = 85

@app.get("/")
def homepage():
    return {"Welcome": "U r at homepage"}

@app.post("/student")
def add_details(record:StudentRecord): 
    database[record.id]  = record   
       
    return {
    "message": "Student added successfully",
    "student_id": record.id
}


@app.post("/details/{student_id}")
def get_details(student_id:int = 0):
    if student_id not in database:
        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )
    return {"Student Details": database[student_id]}
    

@app.get("/predict/{sid}")
def predict(sid: int = 0):
   
    # resp = get_details(student_id=sid)
    # above code doesnt work cuz APi rotes are not functions but HTTP entry points

    record = database[sid]

    score = (
        (record.daily_study_hour / 14) * 40 +
        (record.attendance_percent/ 100) * 20 +
        (record.previous_marks/ 100) * 40
    )
    
    if score >= 80:
        result = "Excellent"
    elif score >= 60:
        result = "Good"
    elif score >= 40:
        result = "Average"
    else:
        result = "Needs Improvement"

    return {
        "score": round(score, 2),
        "prediction": result
    }

