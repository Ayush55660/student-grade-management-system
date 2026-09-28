students = []
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade,
        "Result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_students():
    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("\nName:", student["Name"])
        print("Roll No:", student["Roll No"])
        print("Marks:", student["Marks"])
        print("Total:", student["Total"])
        print("Percentage:", student["Percentage"], "%")
        print("Grade:", student["Grade"])
        print("Result:", student["Result"])

def main():
    while True:
        print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


main()