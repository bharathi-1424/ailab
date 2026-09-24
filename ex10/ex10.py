import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# -------------------------------
# STEP 1: Create Student Dataset
# -------------------------------

data = {
    "Attendance": [95, 88, 76, 60, 92, 70, 85, 55, 98, 65,
                   82, 74, 90, 58, 80, 93, 68, 87, 72, 96],

    "Study_Hours": [6, 5, 3, 1, 6, 2, 5, 1, 7, 2,
                    4, 3, 5, 1, 4, 6, 2, 5, 3, 7],

    "Previous_Marks": [92, 85, 72, 50, 90, 62, 84, 45, 95, 55,
                       78, 70, 88, 48, 75, 94, 60, 86, 68, 96],

    "Assignment_Score": [95, 88, 75, 45, 92, 65, 86, 40, 98, 50,
                         80, 72, 90, 42, 78, 96, 58, 89, 70, 97],

    "Performance": [
        "Good", "Good", "Average", "Poor", "Good",
        "Average", "Good", "Poor", "Good", "Poor",
        "Good", "Average", "Good", "Poor", "Average",
        "Good", "Poor", "Good", "Average", "Good"
    ]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

print("==============================================")
print("   AI BASED STUDENT PERFORMANCE PREDICTION")
print("==============================================")

print("\nStudent Dataset:")
print(df)

# -------------------------------
# STEP 2: Select Input and Output
# -------------------------------

X = df[
    ["Attendance",
     "Study_Hours",
     "Previous_Marks",
     "Assignment_Score"]
]

y = df["Performance"]

# -------------------------------
# STEP 3: Split the Dataset
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -------------------------------
# STEP 4: Create AI Model
# -------------------------------

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# -------------------------------
# STEP 5: Test the Model
# -------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n----------------------------------------------")
print("AI MODEL TRAINING COMPLETED")
print("----------------------------------------------")

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# -------------------------------
# STEP 6: Get New Student Details
# -------------------------------

print("\n==============================================")
print("       ENTER NEW STUDENT DETAILS")
print("==============================================")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

attendance = float(
    input("Enter Attendance Percentage: ")
)

study_hours = float(
    input("Enter Study Hours Per Day: ")
)

previous_marks = float(
    input("Enter Previous Exam Marks: ")
)

assignment_score = float(
    input("Enter Assignment Score: ")
)

# -------------------------------
# STEP 7: Create New Student Data
# -------------------------------

new_student = pd.DataFrame({
    "Attendance": [attendance],
    "Study_Hours": [study_hours],
    "Previous_Marks": [previous_marks],
    "Assignment_Score": [assignment_score]
})

# -------------------------------
# STEP 8: Predict Performance
# -------------------------------

prediction = model.predict(new_student)

predicted_result = prediction[0]

# -------------------------------
# STEP 9: Display Student Result
# -------------------------------

print("\n==============================================")
print("             PREDICTION RESULT")
print("==============================================")

print("Student Name       :", name)
print("Roll Number        :", roll_no)
print("Attendance         :", attendance, "%")
print("Study Hours/Day    :", study_hours)
print("Previous Marks     :", previous_marks, "%")
print("Assignment Score   :", assignment_score, "%")

print("----------------------------------------------")
print("Predicted Performance :", predicted_result)
print("----------------------------------------------")

# -------------------------------
# STEP 10: Give Suggestions
# -------------------------------

if predicted_result == "Good":

    print("Status: Excellent performance.")
    print("Suggestion: Continue the same study habits.")

elif predicted_result == "Average":

    print("Status: Average performance.")
    print("Suggestion: Improve study hours and attendance.")

else:

    print("Status: Poor performance.")
    print("Suggestion: Need more practice and academic support.")

print("\n==============================================")
print("        PREDICTION COMPLETED SUCCESSFULLY")
print("==============================================")