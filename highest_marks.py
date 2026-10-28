marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}
highest = max(marks.values())
for  student_name in marks:
    if marks[student_name] == highest:
        print(student_name, highest)