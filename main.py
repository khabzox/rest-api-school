# imports
from fastapi import FastAPI
from pydantic import BaseModel

# Create App FastAPI
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define model of Data using Pydantic
class Student(BaseModel):
    id: int
    name: str
    grade: int

# list for saveing data in memory
students = [
    Student(id=1, name="Karim ali", grade=5),
    Student(id=2, name="khadija ahmed", grade=3),
]

# Read all items
@app.get("/students/")
def read_students():
    return students

# Create new student
@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

# Update item by ID using PUT Method
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

# Delete item by ID using DELETE Method
@app.delete("/students/{student_id}")
def delete_student(student_id: int, deleted_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"meddage": "Student Deleted"}
    return {"error": "Student not found"}