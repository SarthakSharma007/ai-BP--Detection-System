# 🩺 Fast Detection of Blood Pressure by Scanning Symptoms

This project is a machine learning-based web application that predicts the likelihood of high or low blood pressure based on symptoms provided by the user. The model is trained using collected data and deployed in a user-friendly web interface.

---

## 📌 Features

- Predicts blood pressure risk based on user inputs  
- Machine learning model trained with symptom data  
- Simple and clean web interface  
- Runs locally or can be hosted online  
- Instant results for given readings  

---

## 🛠️ Tech Stack

- **Python** – Core programming language  
- **Flask** – Backend web framework  
- **Scikit-learn / Pandas / NumPy** – For machine learning model training and prediction  
- **HTML / CSS / JavaScript** – Frontend interface  

---

## 📂 Project Structure

 ├── model.py            # Trains and saves the ML model ├── app.py              # Flask app to handle requests and predictions ├── templates/          # HTML frontend files │   └── index.html ├── static/             # CSS and JS files for styling and interaction ├── bp_dataset.csv      # Dataset used for model training ├── requirements.txt    # Python dependencies └── README.md           # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/blood-pressure-detection.git
cd blood-pressure-detection

2️⃣ Install dependencie
pip install -r requirements.txt

3️⃣ Train the model (optional if model.pkl is provided
python model.py
4️⃣ Run the applicatio
python app.py
5️⃣ Open in browser
Visit http://127.0.0.1:5000 in your web browser.

📊 How It Works
- User enters symptom data (e.g., headache severity, dizziness level, etc.)
- The backend ML model processes the input
- The prediction result (High BP / Low BP / Normal) is displayed instantly

📝 Example Input & Output
Input:
Headache: 7  
Dizziness: 3  
Blurred Vision: 5


Output:
Prediction: High Blood Pressure Risk



📬 Contributing
Feel free to fork the repo, raise issues, or submit pull requests to improve the project!
