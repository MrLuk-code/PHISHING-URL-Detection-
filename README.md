# 🔎 Phishing URL Detection

A machine learning-based project to detect and classify phishing URLs. Phishing websites are fraudulent sites designed to steal sensitive user data such as usernames, passwords, and credit card details. This project applies data preprocessing, feature extraction, and machine learning techniques to distinguish between legitimate and phishing URLs.


---

# #🚀 Features

Extracts URL-based features (e.g., length, presence of @, HTTPS, domain age).

Trains machine learning models (Random Forest, Logistic Regression, etc.) for classification.

Provides metrics such as accuracy, precision, recall, and F1-score.

Can be extended into a web app or API for real-time detection.



---
```
📂 Project Structure

phishing-url-detection/
│
├── data/                 # Dataset files (CSV, etc.)
├── notebooks/            # Jupyter notebooks for experiments
├── src/                  # Source code for preprocessing, training & evaluation
│   ├── features.py       # Feature extraction from URLs
│   ├── model.py          # Training & testing ML models
│   └── utils.py          # Helper functions
├── results/              # Model performance reports & plots
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

```
---

# ⚙️ Installation

**Clone this repository:**

git clone https://github.com/your-username/phishing-url-detection.git
cd phishing-url-detection

**Create a virtual environment (recommended):**

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

Install dependencies:

pip install -r requirements.txt


---

📊 Usage

Run feature extraction and training:

python src/model.py

Test with a custom URL:

from src.features import extract_features
from src.model import load_model, predict

url = "http://example.com/login"
features = extract_features(url)
model = load_model("results/phishing_model.pkl")
print(predict(model, features))


---

📈 Results

Random Forest Accuracy: 95%

Logistic Regression Accuracy: 91%

SVM Accuracy: 93%


(Detailed results are available in the results/ folder.)


---

📚 Dataset

This project uses publicly available phishing and legitimate URL datasets:

PhishTank

UCI ML Repository

Kaggle - Phishing Dataset



---

🔮 Future Work

Develop a Flask/Django web application for real-time detection.

Deploy as a browser extension for end-users.

Improve feature engineering with NLP & deep learning models.



---

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or create an issue.


---

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.


---
