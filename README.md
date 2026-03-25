# Cyberbullying Detection Using Machine Learning

## Problem Statement (Social Media Platforms)

With the rapid growth of social media platforms, online communication has increased significantly. However, many users post harmful, abusive, or offensive messages that can lead to cyberbullying. Cyberbullying can negatively affect individuals emotionally and psychologically.

Most platforms still depend on manual monitoring of messages, which is:

- Time consuming
- Difficult to monitor large amounts of data
- Human moderators may miss harmful content

So there is a need for an automatic cyberbullying detection system to identify harmful messages quickly.

---

## What We Came Up With (Solution)

We developed a **Cyberbullying Detection System using Machine Learning**.  
This project helps automatically detect whether a message contains cyberbullying or not.

The system processes text data and uses machine learning models to classify messages as **Cyberbullying** or **Non-Cyberbullying**.

It provides a GUI-based application where users can enter a message and view the detection result.

---

## Project Workflow

1. Load the cyberbullying tweets dataset
2. Perform text preprocessing (cleaning and removing unwanted characters)
3. Convert text into numerical features using TF-IDF vectorization
4. Split the dataset into training and testing sets
5. Train machine learning models
6. Compare model performance using accuracy
7. User enters a message
8. System predicts whether it is cyberbullying or not

---

## Dataset

The dataset contains tweets labeled as cyberbullying or non-cyberbullying.

Dataset includes:

- Tweet text
- Cyberbullying category

The dataset is used for training and testing the machine learning models.

---

## Model & Evaluation

Machine learning algorithms used:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

Model performance is evaluated using:

- Accuracy score

---

## Features

- Load and analyze tweet dataset
- Text preprocessing
- Train machine learning models
- Compare model accuracy
- Predict cyberbullying in user messages
- GUI application for detection

---

## Tech Stack

- Python
- Scikit-learn
- Pandas
- Tkinter
- Matplotlib

---

## How to Run

### 1 Install required libraries
