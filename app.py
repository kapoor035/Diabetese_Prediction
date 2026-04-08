from flask import Flask, render_template, request # type: ignore
import pickle
import numpy as np # type: ignore
filename = 'diabetes-prediction-rfc-model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = model.predict(data)
        # print("Prediction successful")
        
        return render_template('result.html', prediction=my_prediction, message=("High Risk of Diabetes" if my_prediction[0] == 1 else "Low Risk of Diabetes"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)