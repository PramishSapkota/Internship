from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Predicting student result",
    description="Dictionary stores real values not objects",
    version="2",)

database = {0:{
                "id": 0,
                "name": "Bipin",
                "daily_study_hour":10,
                "attendance_percent":90,
                "previous_marks": 92,
                } 
            }

class StudentRecord(BaseModel):
    id:int = 1
    name:str = "Ram"
    daily_study_hour:int = 8
    attendance_percent:float = 75
    previous_marks: float = 85

@app.get("/")
def homepage():
    return {"Welcome": "U r at homepage"}

@app.post("/student")
def add_details(record:StudentRecord): 
    database[record.id]  = {
                            "id":record.id,
                            "name": record.name,
                            "daily_study_hour":record.daily_study_hour,
                            "attendance_percent":record.attendance_percent,
                            "previous_marks": record.previous_marks,
                           } 
    return {
    "message": "Student added successfully",
    "student_id": record.id
}


@app.get("/details/{student_id}")
def get_details(student_id:int = 0):
    if student_id not in database:
        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )
    # details = (
    #     f"\nId: {database[student_id].id}"
    #     f"\nDaily Study Hour: {database[student_id].daily_study_hour}"
    #     f"\nAttendance Percent: {database[student_id].attendance_percent}"
    #     f"\nPrevious Marks: {database[student_id].previous_marks}"
    # )

    # return {"Student Details": details}
    return {"Student Details": database[student_id]}
    

@app.get("/predict/{sid}")
def predict(sid: int = 0):
   
    # resp = get_details(student_id=sid)
    # above code doesnt work cuz APi rotes are not functions but HTTP entry points

    record = database[sid]

    score = (
        (record['daily_study_hour'] / 14) * 40 +
        (record['attendance_percent'] / 100) * 20 +
        (record['previous_marks'] / 100) * 40
    )
    # if i had stored the pydantic object in database then i would have to access with dot operator as:
    # record.daily_study_hour instead of record['daily_study_hour']

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

