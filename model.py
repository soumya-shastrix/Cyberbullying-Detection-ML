import pandas as pd
import re
import nltk
import warnings
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Suppress warnings and download stopwords
warnings.filterwarnings('ignore')
nltk.download('stopwords')

# === Load and Prepare Data ===
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Load dataset
df = pd.read_csv("cyberbullying_tweets.csv")  # Ensure this CSV is present
df = df[['tweet_text', 'cyberbullying_type']]
df['label'] = df['cyberbullying_type'].apply(lambda x: 0 if x == 'not_cyberbullying' else 1)

# Clean text function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

df['cleaned_text'] = df['tweet_text'].apply(clean_text)

# === Vectorize and Split Data ===
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['cleaned_text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Train Models ===
lr_model = LogisticRegression().fit(X_train, y_train)
svm_model = SVC(kernel='linear').fit(X_train, y_train)
rf_model = RandomForestClassifier().fit(X_train, y_train)
xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', n_estimators=100, max_depth=3).fit(X_train, y_train)

# === Accuracy Scores ===
model_accuracies = {
    "SVM": accuracy_score(y_test, svm_model.predict(X_test)),
    "Random Forest": accuracy_score(y_test, rf_model.predict(X_test)),
    "Logistic Regression": accuracy_score(y_test, lr_model.predict(X_test)),
    "XGBoost": accuracy_score(y_test, xgb_model.predict(X_test)),
}

model_objects = {
    "SVM": svm_model,
    "Random Forest": rf_model,
    "Logistic Regression": lr_model,
    "XGBoost": xgb_model
}

# === Prediction Function ===
def predict_text(text, model):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    return "Cyberbullying" if pred == 1 else "Not Cyberbullying"

# === Tkinter GUI ===
def launch_gui():
    root = tk.Tk()
    root.title("Cyberbullying Detection App")
    root.geometry("900x550")
    root.configure(bg="#e0f7fa")

    frame = tk.Frame(root, bg="#e0f7fa", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Cyberbullying Detection System", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#00796b")
    title.pack(pady=10)

    input_label = tk.Label(frame, text="Enter Tweet Text:", font=("Arial", 14), bg="#e0f7fa")
    input_label.pack(anchor="w")
    entry_text = tk.Entry(frame, font=("Arial", 14), width=70)
    entry_text.pack(pady=10)

    result_frames = {}
    result_labels = {}

    for model_name in model_objects:
        f = tk.Frame(frame, bg="#ffffff", relief="groove", bd=2, padx=10, pady=5)
        f.pack(pady=5, fill="x")
        lbl = tk.Label(f, text=f"{model_name}: Pending", font=("Arial", 14), bg="#ffffff")
        lbl.pack(anchor="w")
        result_frames[model_name] = f
        result_labels[model_name] = lbl

    def show():
        text = entry_text.get()
        for model_name, model in model_objects.items():
            prediction = predict_text(text, model)
            accuracy = model_accuracies[model_name] * 100
            color = "#d32f2f" if prediction == "Cyberbullying" else "#388e3c"
            bg_color = "#ffebee" if prediction == "Cyberbullying" else "#e8f5e9"
            result_labels[model_name].config(
                text=f"{model_name}: {prediction}  |  Accuracy: {accuracy:.2f}%",
                fg=color,
                bg=bg_color
            )
            result_frames[model_name].config(bg=bg_color)

    btn = tk.Button(frame, text="Classify", command=show, font=("Arial", 14), bg="#00796b", fg="white", padx=10, pady=5)
    btn.pack(pady=10)

    root.mainloop()

# === Terminal Live Input ===
def live_terminal_input():
    print("\n🔍 Live Cyberbullying Detection (type 'exit' to stop)")
    while True:
        user_input = input("\nEnter a message: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        for name, model in model_objects.items():
            prediction = predict_text(user_input, model)
            print(f"→ {name}: {prediction} (Accuracy: {model_accuracies[name]*100:.2f}%)")

# === Main Choice ===
if __name__ == "__main__":
    print("Choose how you want to test the detection system:")
    print("1. GUI (Window Interface)")
    print("2. Terminal Live Input")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        launch_gui()
    else:
        live_terminal_input()
