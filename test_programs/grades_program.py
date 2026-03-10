# grades_program.py - intentionally broken
students = {
"Alice": 85,
"Bob": 90,
"Charlie": 78
}

for name, score in students.items():
    print(f"{name} scored {score}")

average = sum(students.values()) / len(students)
print("Average score:", average)