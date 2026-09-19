# Importing all the libraries

import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# This Function gives any recomendations for the students (Based on the comd)
def recommendation(student):
    recommendations = []
    if student["StudyHours"] < 2:
        recommendations.append("Increase regular study time")
    if student["Attendance"] < 75:
        recommendations.append("Improve attendance")
    if student["AssignmentScore"] < 50:
        recommendations.append("Focus on completing assignments")
    if student["PreviousMarks"] < 50:
        recommendations.append("Revise previous concepts")
    if len(recommendations) == 0:
        recommendations.append("Maintain current academic habits")

    return recommendations

# This function gives the support level of the student that they need
def support_level(score):
    if score < 40:
        return "HIGH SUPPORT"
    elif score < 60:
        return "MODERATE SUPPORT"
    else:
        return "LOW/NO SUPPORT"

# Main Program

# Reading the json file
# THE DATA IS GIVEN BY AI FOR CREATING THE EQUATION

df = pd.read_json("student_performance_500_no_participation_no_NA.json")

# Assigning the input and output

X = df[[
    "StudyHours",
    "Attendance",
    "PreviousMarks",
    "AssignmentScore",
    "SleepHours"
]]
Y = df["FinalScore"]

# Splitting  Training and Testing data

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, Y_train)

# Evaluation of the Model

mae = mean_absolute_error(Y_test, model.predict(X_test))
mse = mean_squared_error(Y_test, model.predict(X_test))
r2 = r2_score(Y_test, model.predict(X_test))

print("\nModel Evaluation")

print("Mean Absolute Error : ", mae)
print("Mean Squared Error : ", mse)
print("R² : ", r2)

# Displaying the Equation of the Model

c1 = model.coef_[0]
c2 = model.coef_[1]
c3 = model.coef_[2]
c4 = model.coef_[3]
c5 = model.coef_[4]
k = model.intercept_

print("\nModel Equation : ")
print(f"FinalScore = {c1:.2f}*StudyHours + {c2:.2f}*Attendence + {c3:.2f}*PreviousMarks + {c4:.2f}*AssinmentScores + {c5:.2f}*SleepHours + {k:.2f}")

# To Predict the FinalScore for a user input using the equation found

StudyHours = float(input("Enter the Study Hours of the Student : "))
Attendance = float(input("Enter the Attendence of the Student for 100% : "))
PreviousMarks = float(input("Enter the Previous Marks of the Student out of 100 : "))
AssignmentScore = float(input("Enter the Assignment Scores of the Student out of 100 : "))
SleepHours = float(input("Enter the Sleep Hours of the Student : "))

FinalScore = c1*StudyHours + c2*Attendance + c3*PreviousMarks + c4*AssignmentScore + c5*SleepHours + k

print("\nFinalScore : " , FinalScore)

print("Support Level : " , support_level(FinalScore))

student = {
    "StudyHours" :  StudyHours ,
    "Attendance" : Attendance ,
    "PreviousMarks" : PreviousMarks,
    "AssignmentScore" : AssignmentScore ,
    "SleepHours" : SleepHours
}
i = 0
student_rec = recommendation(student)
for i in range(len(student_rec)) :
    print("-",student_rec[i])
    i += 1 
