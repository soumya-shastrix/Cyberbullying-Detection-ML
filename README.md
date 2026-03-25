Cyberbullying Detection using Machine Learning
This project focuses on detecting cyberbullying in online messages using machine learning techniques. Social media platforms often contain harmful or abusive comments, and this system helps identify such messages automatically.
In this project, a dataset of tweets is used to train machine learning models that can classify whether a message contains cyberbullying or not. The text data is first cleaned and prepared, and then converted into numerical features using TF-IDF so that machine learning models can understand the text.
Different machine learning algorithms are trained and tested to compare their performance in identifying cyberbullying messages.
The project also provides a user interface where users can enter a tweet or message and check whether it is classified as cyberbullying or not.

Features
Data preprocessing and cleaning 
Text feature extraction using TF-IDF 
Multiple machine learning classification models 
Accuracy comparison between models 
GUI application for message testing 
Streamlit interface for real-time detection 

Machine Learning Models Used
Logistic Regression 
Support Vector Machine (SVM) 
Random Forest 
XGBoost 
These models are trained on tweet data to predict whether a message contains cyberbullying. 

Technologies Used
Python 
Scikit-learn 
Pandas 
NLTK 
Tkinter 
Streamlit 
Matplotlib 

Dataset
The dataset used in this project contains tweets labeled as cyberbullying or non-cyberbullying. The model learns patterns from this dataset and uses them to classify new messages. 


How to Run the Project

Clone the repository

git clone https://github.com/yourusername/Cyberbullying-Detection-ML

Install required libraries

pip install pandas numpy scikit-learn nltk xgboost streamlit
Run the main application

python main.py

or run the Streamlit interface

streamlit run stream.py

Conclusion
This project shows how machine learning models can be used to automatically detect cyberbullying messages. Such systems can help reduce harmful online interactions and make digital platforms safe
