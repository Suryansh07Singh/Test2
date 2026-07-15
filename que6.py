import students_utils
import json

students = [
    ("Rahul", [85, 90, 88]),
    ("Priya", [78, 82, 80]),
    ("Amit", [92, 95, 89])
]

report = []

for student in students:
    name, marks = student
    avg = students_utils.calculate_average(*marks)
    grade = students_utils.get_grade(avg)
    report.append(f"Name: {name} | Average: {avg:.2f} | Grade: {grade}")

with open("report.txt", "w") as f:
    for line in report:
        f.write(line + "\n")

with open("students.json", "w") as f:
    json.dump(students, f)

print("Contents of report.txt:")
with open("report.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line.strip()}")

print("\nContents of students.json:")
with open("students.json", "r") as f:
    data = json.load(f)
    for student in data:
        print(student)