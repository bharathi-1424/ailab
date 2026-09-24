# AI BASED STUDENT PERFORMANCE PREDICTION SYSTEM

import math


# Function to calculate attendance score
def calculate_attendance_score(attendance):
    if attendance >= 90:
        return 20
    elif attendance >= 75:
        return 15
    elif attendance >= 60:
        return 10
    else:
        return 5


# Function to calculate study score
def calculate_study_score(study_hours):
    if study_hours >= 6:
        return 20
    elif study_hours >= 4:
        return 15
    elif study_hours >= 2:
        return 10
    else:
        return 5


# Function to calculate previous mark score
def calculate_mark_score(previous_marks):
    if previous_marks >= 85:
        return 20
    elif previous_marks >= 70:
        return 15
    elif previous_marks >= 50:
        return 10
    else:
        return 5


# Function to calculate assignment score
def calculate_assignment_score(assignment):
    if assignment >= 85:
        return 15
    elif assignment >= 70:
        return 12
    elif assignment >= 50:
        return 8
    else:
        return 5


# Function to calculate internal assessment score
def calculate_internal_score(internal):
    if internal >= 85:
        return 25
    elif internal >= 70:
        return 20
    elif internal >= 50:
        return 15
    else:
        return 5


# Function to predict performance
def predict_performance(total_score):

    if total_score >= 80:
        return "GOOD"

    elif total_score >= 60:
        return "AVERAGE"

    else:
        return "POOR"


# Function to provide suggestion
def give_suggestion(performance):

    if performance == "GOOD":
        return "Excellent performance. Continue the same study habits."

    elif performance == "AVERAGE":
        return "Improve study time and academic performance."

    else:
        return "Need more practice and regular study."


# Main Program
def main():

    print("====================================================")
    print("       AI BASED STUDENT PERFORMANCE PREDICTION")
    print("====================================================")

    # Student details
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    print("\nEnter Student Academic Details")
    print("--------------------------------------------")

    attendance = float(input("Enter Attendance Percentage: "))
    study_hours = float(input("Enter Study Hours Per Day: "))
    previous_marks = float(input("Enter Previous Exam Marks: "))
    assignment = float(input("Enter Assignment Score: "))
    internal = float(input("Enter Internal Assessment Marks: "))

    # Calculate individual scores
    attendance_score = calculate_attendance_score(attendance)
    study_score = calculate_study_score(study_hours)
    mark_score = calculate_mark_score(previous_marks)
    assignment_score = calculate_assignment_score(assignment)
    internal_score = calculate_internal_score(internal)

    # Calculate total score
    total_score = (
        attendance_score +
        study_score +
        mark_score +
        assignment_score +
        internal_score
    )

    # Predict performance
    performance = predict_performance(total_score)

    # Get suggestion
    suggestion = give_suggestion(performance)

    # Display result
    print("\n====================================================")
    print("                PREDICTION RESULT")
    print("====================================================")

    print("Student Name          :", name)
    print("Roll Number           :", roll_no)
    print("Department            :", department)
    print("Attendance            :", attendance, "%")
    print("Study Hours Per Day   :", study_hours)
    print("Previous Exam Marks   :", previous_marks)
    print("Assignment Score      :", assignment)
    print("Internal Marks        :", internal)

    print("----------------------------------------------------")

    print("Attendance Score      :", attendance_score)
    print("Study Score           :", study_score)
    print("Previous Mark Score   :", mark_score)
    print("Assignment Score      :", assignment_score)
    print("Internal Score        :", internal_score)

    print("----------------------------------------------------")

    print("Total Performance Score :", total_score, "/ 100")
    print("Predicted Performance   :", performance)
    print("Suggestion              :", suggestion)

    print("====================================================")
    print("       PREDICTION COMPLETED SUCCESSFULLY")
    print("====================================================")


# Program execution
if __name__ == "__main__":
    main()