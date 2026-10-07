# FASTAPI
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student (BaseModel):
    id: str
    age: int
    grade: str
students =[ 
    student ( id="ahmed", age=20, grade="A"), 
    student ( id="joo", age=22, grade="B"),
    ]
@app.get("/students")
def read_students():
    return students
@app.post("/students")
def create_student(new_student: student):
    students.append(new_student)
    return new_student
@app.put("/students/{student_id}")
def update_student(student_id: str, updated_student: student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated_student
            return updated_student
    return {"error": "Student not found"}
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    for i, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(i)
            return deleted_student
    return {"error": "Student not found"}