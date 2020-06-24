  
from flask import Flask, render_template, jsonify, request
import joblib
import pandas as pd
import json
import pickle
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/data_visualization')
def data_visualization():
    return render_template('DataVisual.html')

@app.route('/prediction')
def model():
    return render_template('prediction.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        Credit = int(input['Amount given Credit'])
        
        Marital = input['Marital Status']
        if Marital == '1':
            inputMRT = 1
            strMRT = 'Married'
        elif Marital == '2':
            inputMRT = 2
            strMRT = 'Single'
        elif Marital == '3':
            inputMRT = 3
            strMRT = 'Others'
        
        Bill = int(input['Total Bill'])

        MPL = int(input['Mean Pay Late'])

        RepaySep = int(input['Repayment Sep'])

        Pay = int(input['Total Pay'])

        input_predict = pd.DataFrame({
            'Amount given Credit' : [Credit],
            'Marital Status' : [inputMRT],
            'Total Bill' : [Bill],
            'Mean Pay Late' : [MPL],
            'Repayment Sep' : [RepaySep],
            'Total Pay' : [Pay]
            
        })

        predict = model.predict(input_predict)[0]

        if predict == 0:
            result = 'Negative'
        elif predict == 1:
            result = 'Positive'

        return render_template('result.html', Credit = Credit, Marital = strMRT, Bill = Bill, MPL = MPL,
                RepaySep = RepaySep, Pay = Pay, result=result)

if __name__ == '__main__':
    model = pickle.load(open('finalmodel.pkl', 'rb'))
    app.run(debug=True)