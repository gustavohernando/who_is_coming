from flask import Flask, render_template, request
import pickle
from datetime import date
from datetime import datetime
import numpy as np
from utils.libreria import  transformacion

model = pickle.load(open('utils/gradient_boosting.model', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    Scheduled_date = transformacion(request.form['Variable 1'])
    Appointment_date = transformacion(request.form['Variable 2'])
    Scholarship_raw = request.form['Variable 3']
    Gender_index_raw = request.form['Variable 4']
    Hipertension_raw = request.form['Variable 5']
    data4 = request.form['Variable 6']
    data5 = request.form['Variable 5']
    data6 = request.form['Variable 6']
    arr = np.array([[data1, data2, data3, data4, data4, data6]])
    pred = model.predict(arr)
    return render_template('gambas.html', variable=pred)

def transformacion(fecha_en_crudo):#dd/mm/aaaa --:--
    dia=fecha_en_crudo[:2]
    mes=fecha_en_crudo[3:5]
    año=fecha_en_crudo[6:10]
    hora=fecha_en_crudo[11:13]
    minuto=fecha_en_crudo[14:16]
    return int(dia),int(mes),int(año),int(hora),int(minuto)



if __name__ == "__main__":
    app.run(debug=True)