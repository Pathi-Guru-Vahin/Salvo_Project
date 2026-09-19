# Salvo_Project
# Student Performance Prediction using Linear Regression

A Machine Learning project that predicts a student's **Final Score** using academic and lifestyle factors such as study hours, attendance, previous marks, assignment scores, and sleep hours.

The project also identifies the student's **required support level** and provides **personalized recommendations** based on their input.

---

## Project Overview

The goal of this project is to use **Linear Regression** to predict a student's final academic performance.

The model learns the relationship between:

* Study Hours
* Attendance
* Previous Marks
* Assignment Score
* Sleep Hours

and the target variable:

* **Final Score**

After training, the program allows the user to enter information about a student and predicts their expected final score.

It then:

1. Predicts the student's Final Score.
2. Determines their Support Level.
3. Provides recommendations to improve their academic performance.

---

##  Machine Learning Model

This project uses **Multiple Linear Regression**.

The model follows the equation:

```text
FinalScore = c1 × StudyHours
           + c2 × Attendance
           + c3 × PreviousMarks
           + c4 × AssignmentScore
           + c5 × SleepHours
           + Intercept
```

The coefficients (`c1`, `c2`, etc.) are learned automatically from the dataset.

---

## Project Structure

```text
Student-Performance-Prediction/
│
├── Main_Project.py
├── student_performance_500_no_participation_no_NA.json
└── README.md
```

### Files

| File                                                  | Description                                                      |
| ----------------------------------------------------- | ---------------------------------------------------------------- |
| `Main_Project.py`                                     | Main Python program containing the ML model and prediction logic |
| `student_performance_500_no_participation_no_NA.json` | Dataset containing student performance records                   |
| `README.md`                                           | Project documentation                                            |

---

## Dataset

The project uses a JSON dataset containing approximately **500 student records**.

### Input Features

| Feature           | Description                      |
| ----------------- | -------------------------------- |
| `StudyHours`      | Number of hours spent studying   |
| `Attendance`      | Student attendance percentage    |
| `PreviousMarks`   | Marks obtained previously        |
| `AssignmentScore` | Assignment score                 |
| `SleepHours`      | Average number of hours of sleep |

### Target Variable

| Variable     | Description                    |
| ------------ | ------------------------------ |
| `FinalScore` | Student's final academic score |

---

## Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **JSON Dataset**
* **Linear Regression**

### Python Libraries

```python
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

---

## How the Project Works

### 1. Load the Dataset

The program reads the JSON dataset using Pandas:

```python
df = pd.read_json("student_performance_500_no_participation_no_NA.json")
```

---

### 2. Select Input and Output Variables

The following five features are used as inputs:

```text
StudyHours
Attendance
PreviousMarks
AssignmentScore
SleepHours
```

The target variable is:

```text
FinalScore
```

---

### 3. Split the Dataset

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

using:

```python
train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42
)
```

---

### 4. Train the Model

A Linear Regression model is created:

```python
model = LinearRegression()
```

The model is then trained using:

```python
model.fit(X_train, Y_train)
```

---

### 5. Evaluate the Model

The model is evaluated using three metrics:

### Mean Absolute Error (MAE)

Measures the average absolute difference between the predicted and actual scores.

```python
mae = mean_absolute_error(Y_test, model.predict(X_test))
```

Lower MAE generally means smaller prediction errors.

### Mean Squared Error (MSE)

Measures the average squared difference between predicted and actual values.

```python
mse = mean_squared_error(Y_test, model.predict(X_test))
```

Lower MSE indicates smaller prediction errors.

### R² Score

Measures how much of the variation in Final Score is explained by the model.

```python
r2 = r2_score(Y_test, model.predict(X_test))
```

An R² value closer to 1 indicates that the model explains more of the variation in the target data.

---

## Model Equation

After training, the program extracts the coefficients:

```python
c1 = model.coef_[0]
c2 = model.coef_[1]
c3 = model.coef_[2]
c4 = model.coef_[3]
c5 = model.coef_[4]
k = model.intercept_
```

It then displays the learned equation:

```text
FinalScore = c1*StudyHours
           + c2*Attendance
           + c3*PreviousMarks
           + c4*AssignmentScore
           + c5*SleepHours
           + k
```

This makes the model easier to understand because the contribution of each feature can be examined through its coefficient.

---

# Student Prediction

After training the model, the program asks the user to enter information about a student.

Example:

```text
Enter the Study Hours of the Student : 4
Enter the Attendence of the Student for 100% : 85
Enter the Previous Marks of the Student out of 100 : 72
Enter the Assignment Scores of the Student out of 100 : 80
Enter the Sleep Hours of the Student : 7
```

The program calculates the predicted Final Score using the learned regression equation.

Example output:

```text
FinalScore : 76.42
```

---

# Student Support Level

The project also categorizes students according to their predicted Final Score.

```python
def support_level(score):
    if score < 40:
        return "HIGH SUPPORT"
    elif score < 60:
        return "MODERATE SUPPORT"
    else:
        return "LOW/NO SUPPORT"
```

### Support Categories

| Predicted Score | Support Level    |
| --------------: | ---------------- |
|        Below 40 | HIGH SUPPORT     |
|      40 – 59.99 | MODERATE SUPPORT |
|     60 or above | LOW/NO SUPPORT   |

This feature can help identify students who may need additional academic attention.

> **Note:** These thresholds are project-defined rules and should not be treated as validated educational or institutional standards.

---

# Student Recommendations

The program generates recommendations based on the student's input.

### Study Hours

If:

```text
StudyHours < 2
```

Recommendation:

```text
Increase regular study time
```

### Attendance

If:

```text
Attendance < 75
```

Recommendation:

```text
Improve attendance
```

### Assignment Score

If:

```text
AssignmentScore < 50
```

Recommendation:

```text
Focus on completing assignments
```

### Previous Marks

If:

```text
PreviousMarks < 50
```

Recommendation:

```text
Revise previous concepts
```

If none of the conditions are triggered:

```text
Maintain current academic habits
```

---

# Example Output

```text
Model Evaluation

Mean Absolute Error : 4.58
Mean Squared Error : 31.95
R² : 0.59

Model Equation :

FinalScore = 2.75*StudyHours
           + 0.22*Attendance
           + 0.26*PreviousMarks
           + 0.16*AssignmentScore
           + 0.62*SleepHours
           + 11.84

Enter the Study Hours of the Student : 3
Enter the Attendence of the Student for 100% : 80
Enter the Previous Marks of the Student out of 100 : 65
Enter the Assignment Scores of the Student out of 100 : 70
Enter the Sleep Hours of the Student : 7

FinalScore : XX.XX

Support Level : LOW/NO SUPPORT

- Maintain current academic habits
```

*The prediction will change depending on the values entered.*

---

# Installation

## 1. Install Python

Install Python from the official Python website.

## 2. Install Required Libraries

Open a terminal and run:

```bash
pip install pandas scikit-learn
```

---

# How to Run

Clone or download this repository.

Make sure the following files are in the same folder:

```text
Main_Project.py
student_performance_500_no_participation_no_NA.json
```

Then run:

```bash
python Main_Project.py
```

The program will:

```text
Load Dataset
     ↓
Select Features
     ↓
Split Training & Testing Data
     ↓
Train Linear Regression Model
     ↓
Evaluate Model
     ↓
Display Regression Equation
     ↓
Take Student Input
     ↓
Predict Final Score
     ↓
Determine Support Level
     ↓
Generate Recommendations
```

---

# Project Features

* JSON-based student dataset
* Multiple Linear Regression
* Train-test data splitting
* Model evaluation using MAE
* Model evaluation using MSE
* Model evaluation using R²
* Automatic regression equation generation
* Student Final Score prediction
* Student support-level identification
* Personalized academic recommendations
* Simple command-line interface

---

# 🔮 Future Improvements

The project can be extended with:

* Graphical User Interface (GUI)
* Web-based interface
* Data visualization
* Feature importance visualization
* Comparison with other ML models
* Random Forest Regression
* XGBoost Regression
* Improved support-level methodology
* More student-related features
* Database integration
* Model saving and loading
* Automatic report generation

---

# Limitations

This project is intended as an **educational Machine Learning project**.

The predictions depend on the quality and representativeness of the dataset. A student's academic performance can also depend on factors that are not included in this model.

The support categories are rule-based thresholds created for this project and are not a substitute for professional academic assessment.

---

# Learning Objectives

Through this project, the following concepts can be demonstrated:

1. Loading and processing JSON data using Pandas.
2. Selecting features and target variables.
3. Splitting data into training and testing sets.
4. Training a Multiple Linear Regression model.
5. Understanding regression coefficients.
6. Evaluating an ML model.
7. Making predictions using a trained model.
8. Applying rule-based logic to ML predictions.
9. Generating recommendations from student data.
10. Understanding a basic end-to-end Machine Learning workflow.

---

##  Project

**Project:** Student Performance Prediction
**Algorithm:** Multiple Linear Regression
**Language:** Python
**Dataset:** Student Performance Dataset
**Purpose:** Educational / Academic ML Project

