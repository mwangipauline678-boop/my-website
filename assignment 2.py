# Asking user to enter student details
admission_number = input("Enter Admission Number: ")
name = input("Enter Name: ")
stream = input("Enter Stream (Science, Arts, Commerce): ")
age = int(input("Enter Age: "))
height = float(input("Enter Height in meters: "))
#storing student details in a dictionary
student = {
    "Admission Number": admission_number,
    "Name": name,
    "Stream": stream,
    "Age": age,
    "Height": height
}
#displaying student details
print("\n--- Student Details ---")
print("Admission Number:", student["Admission Number"])
print("Name:", student["Name"])
print("Stream:", student["Stream"])
print("Age:", student["Age"])
print("Height:", student["Height"], "meters")
#calculating age after 5 years

future_age = student["Age"] + 5
print("\nAge after 5 years:", future_age)
#asking user to enter 3 favorite subjects and sorting them in a list
subjects = []

print("\nEnter your 3 favorite subjects:")
subjects.append(input("Subject 1: "))
subjects.append(input("Subject 2: "))
subjects.append(input("Subject 3: "))
#displaying favourite subjects
print("\n--- Favorite Subjects ---")
for subject in subjects:
    print(subject)