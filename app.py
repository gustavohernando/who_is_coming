from flask import Flask, render_template, request
import pickle
from datetime import date
import numpy as np
from utils.libreria import  transformacion, yesno, gender
#042

model = pickle.load(open('utils/gradient_boosting.model', 'rb'))
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home_v3.html')

@app.route('/predict', methods=['POST'])
def home():
    Scheduled_date = transformacion(request.form['select-schedule'])
    Appointment_date = transformacion(request.form['select-appointment'])
    SMS_received = yesno(request.form['select-Sms'])
    Scholarship = yesno(request.form['select-Scholarship'])
    Hipertension= yesno(request.form['select-Hipertension'])
    Alcoholism = yesno(request.form['select-Alcoholism'])
    Gender_index = gender(request.form["select-Genre"])

    #calculated features
    Appointment_month = Appointment_date[1]
    ScheduledDay_month = Scheduled_date[1]
    ScheduledDay_Hour = Scheduled_date[4]
    WaitingDays = int(-date(Scheduled_date[0],Scheduled_date[1],Scheduled_date[2]) + date(Appointment_date[0],Appointment_date[1],Appointment_date[2]))

    #return trasnformacion [año,mes,dia,day_of_week,hora,minuto]
    x_predict = np.array([Scholarship, Hipertension, Alcoholism, SMS_received,
                          WaitingDays, Appointment_month, ScheduledDay_month,ScheduledDay_Hour,
                          Gender_index])
    pred = model.predict(x_predict)
    return render_template('after_v3.html', variable=pred)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='127.0.0.1', port=8000, debug=True)