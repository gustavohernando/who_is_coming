from flask import Flask, render_template, request
import pickle
from datetime import datetime,date
import numpy as np
import pandas as pd
from utils.libreria import  transformacion, yesno, gender
#042

model = pickle.load(open('utils/gradient_boosting.model', 'rb'))
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home_v3.html')

@app.route('/predict', methods=['POST'])
def home():
    Scheduled_date = transformacion(str(request.form['fecha_cita_pedida']))
    Appointment_date = transformacion(str(request.form['fecha_cita_dada']))
    SMS_received = yesno(request.form['select-Sms'])
    Scholarship = yesno(request.form['select-Scholarship'])
    Hipertension= yesno(request.form['select-Hipertension'])
    Alcoholism = yesno(request.form['select-Alcoholism'])
    Gender_index = gender(request.form["select-Genre"])

    #calculated features
    Appointment_month = Appointment_date[1]
    ScheduledDay_month = Scheduled_date[1]
    ScheduledDay_Hour = Scheduled_date[4]
    WaitingDays = date(Appointment_date[0],Appointment_date[1],Appointment_date[2]) - date(Scheduled_date[0],Scheduled_date[1],Scheduled_date[2])
    WaitingDays = int(WaitingDays.days)

    #return trasnformacion [año,mes,dia,day_of_week,hora,minuto]
    x_predict_arr = np.array([Scholarship, Hipertension, Alcoholism, SMS_received,
                          WaitingDays, Appointment_month, ScheduledDay_month,ScheduledDay_Hour,
                          Gender_index])

    columns = ['Scholarship', 'Hipertension', 'Alcoholism', 'SMS_received',
            'WaitingDays', 'Appointment_month', 'ScheduledDay_month',
            'ScheduledDay_Hour', 'Gender_index']

    #print(x_predict_arr)
    #print(columns)
    x_predict_arr = x_predict_arr.reshape(1, -1)
    x_predict = pd.DataFrame(x_predict_arr,columns=columns)
    #pred = model.predict(x_predict)
    pred = 1
    #print(pred)
    return render_template('after_v3.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
    #For running in a local host
    app.run(host='127.0.0.1', port=8000, debug=True)