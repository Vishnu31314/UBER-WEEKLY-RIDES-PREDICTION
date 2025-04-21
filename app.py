from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("uber_rides.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    inputs = [
        float(request.form['Priceperweek']),
        float(request.form['Population']),
        float(request.form['monthlyincome']),
        float(request.form['Averageparkingpermonth'])
    ]
    prediction = model.predict([inputs])[0]
    return render_template('index.html', prediction_text=f'Predicted Weekly Rides: {int(prediction)}')

if __name__ == "__main__":
    app.run(debug=True)