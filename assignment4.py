# Step 1: Student Details
name = input("Enter student name: ")
admission = input("Enter admission number: ")
stream = input("Enter stream: ")

# Step 2: Subject Marks Entry
subjects = ["Data Structures", "Digital Literacy", "AI", "Networking"]

marks = {}

for subject in subjects:
    score = int(input(f"Enter marks for {subject}: "))
    marks[subject] = score

# Function to assign grades
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "E"

# Step 4: Display Results
print("\n===== STUDENT RESULTS =====")
print("Student Name:", name)
print("Admission Number:", admission)
print("Stream:", stream)

total = 0

print("\nSubject Results:")
for subject, score in marks.items():
    grade = get_grade(score)
    print(subject, "- Marks:", score, "Grade:", grade)
    total += score

# Step 5: Calculate and Display
average = total / len(subjects)

overall_grade = get_grade(average)

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Overall Grade:", overall_grade)