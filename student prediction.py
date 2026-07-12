# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create dataset using a Python dictionary
data = {
    "Hours": [1, 2, 3, 4.5, 5, 6, 7, 8, 9, 10],
    "Scores": [20, 30, 50, 52, 60, 62, 70, 78, 85, 95]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Student Dataset")
print(df)

# Scatter plot
plt.scatter(df["Hours"], df["Scores"])
plt.title("Hours Studied vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.show()

# Prepare data
X = df[["Hours"]]
y = df["Scores"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict score for a student studying 6.5 hours
predicted_score = model.predict([[6.5]])

print("\nPredicted Score for 6.5 hours:")
print(predicted_score[0])

# Predict scores for all students
df["Predicted Score"] = model.predict(X)

# Calculate Error
df["Error"] = df["Scores"] - df["Predicted Score"]

# Display updated DataFrame
print("\nUpdated DataFrame")
print(df)

# Summary statistics
print("\nSummary Statistics")
print(df.describe())

# Final scatter plot
plt.scatter(df["Hours"], df["Scores"], label="Actual Scores")
plt.scatter(df["Hours"], df["Predicted Score"], label="Predicted Scores")

plt.title("Actual vs Predicted Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()

plt.show()