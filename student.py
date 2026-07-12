# Asking the user for student details
admission_number = input("Enter admission number: ")
full_name = input("Enter full name: ")
stream = input("Enter stream (A,B,C,D,E): ")
age = int(input("Enter age: "))

# Storing information in a dictionary
student = {
    "Admission Number": admission_number,
    "Full Name": full_name,
    "Stream": stream,
    "Age": age
}


# Part 2: Subject Marks


# Asking the user to enter marks
maths = float(input("Enter Mathematics marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer Studies marks: "))

# Storing marks in a list
marks = [maths, english, computer]


# Part 3: Calculations


# Calculating total marks
total_marks = sum(marks)

# Calculating average marks
average_marks = total_marks / len(marks)

# Determining pass or fail
if average_marks >= 50:
    result = "PASS"
else:
    result = "FAIL"

# Part 5: Additional Logic

# Checking if student is minor or adult
if age < 18:
    category = "Minor"
else:
    category = "Adult"


# Part 4: Display Report


print("\n===== STUDENT ACADEMIC REPORT =====")

print("Admission Number:", student["Admission Number"])
print("Full Name:", student["Full Name"])
print("Stream:", student["Stream"])
print("Age:", student["Age"])

print("\nSubject Marks")
print("Mathematics:", maths)
print("English:", english)
print("Computer Studies:", computer)

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)
print("Result:", result)
print("Category:", category)