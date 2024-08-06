import json

with open("students_info.json",'r') as file:
    students = json.load(file)
 
student_courses=[]
    
for student in students:
    print(student["name"].title(),student["roll"])
    student_course={}
    student_course["name"] = student["name"].title()  
    student_course["roll"] = student["roll"]
    if student["roll"]%2 == 0:
        student_course["course"] = "PhD"  
    else:
        student_course["course"] = "Master"
    student_courses.append(student_course)   
    
output_file="student_course.json"
with open(output_file, 'w') as file:
    json.dump(student_courses,file, indent=2)