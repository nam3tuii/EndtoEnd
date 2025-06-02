
from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np
import sqlite3
import os
import csv
filename = r"C:\Users\ASUS\Desktop\end2end\Diabetes-prediction deployed\diabetes-prediction-rfc-model.pkl"
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    
    
    if request.method == 'POST':
        fullname= request.form['fullname']
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
        if my_prediction[0] == 1:
            prediction_text = "Nguy cơ mắc bệnh tiểu đường"
        else:
            prediction_text = "Không bị mắc bệnh tiểu đường"
        
        csv_file='history.csv'
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, mode='a', newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["fullname", "pregnancies", "glucose", "bloodpressure", "skinthickness", "insulin", "bmi", "dpf", "age", "prediction"])
            writer.writerow([fullname, preg, glucose, bp, st, insulin, bmi, dpf, age, prediction_text])
        
            
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)