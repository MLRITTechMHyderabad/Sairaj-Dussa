students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

students_dict = dict(students)

bob_marks = students_dict["Bob"]
average_marks = sum(bob_marks) / len(bob_marks)
print(f"Bob's average grade: {average_marks}")

student_averages = {
    name: sum(marks) / len(marks) for name, marks in students_dict.items()
}
highest_average_name = max(student_averages, key=student_averages.get)
highest_average_marks = student_averages[highest_average_name]
print(highest_average_name)

passed_students_count = sum(
    1 for name, marks in students_dict.items() if all(mark >= 50 for mark in marks)
)
print(f"Number of passed students: {passed_students_count}")

passed_count = sum(
    1 for name, marks in studnets
)
