# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to display student information
def show_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Grade:", student["grade"])
    print("Marks:", student["marks"])
    print("Total Marks:", calculate_total(student["marks"]))
    print("Average Marks:", calculate_average(student["marks"]))
    print("-" * 30)


# List of students
students = [
    {
        "name": "Rahul",
        "age": 12,
        "grade": 7,
        "marks": (85, 90, 78)
    },
    {
        "name": "Priya",
        "age": 13,
        "grade": 8,
        "marks": (92, 88, 95)
    }
]

# Loop to display each student
for student in students:
    show_student(student)
