# 1. Dictionary with 5 student name-score pairs
from webbrowser import get


grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 83,
    "Diana": 97,
    "Ethan": 79,
}
total_score = 0
for student in grade_book:
    total_score = grade_book[student]
class_average = total_score / len(grade_book)
print(f"Class Average: {class_average:.2f}")

top_student = max (grade_book, key=grade_book.get)
print(f"Top Student: {top_student} with a score of {grade_book[top_student]}")
bottom_student = min(grade_book, key=grade_book.get)
print(f"Bottom Student: {bottom_student} with a score of {grade_book[bottom_student]}")

search_name = input("enter a students name to look for their score")

student_score = grade_book.get(search_name)

print(f"result: student grade")
