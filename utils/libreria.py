from datetime import date
from datetime import datetime

def transformacion(fecha_en_crudo):#2021-10-15T05:45:57
    print(fecha_en_crudo)
    dia=int(fecha_en_crudo[8:10])
    mes=int(fecha_en_crudo[5:7])
    año=int(fecha_en_crudo[0:4])
    hora=int(fecha_en_crudo[11:13])
    minuto=int(fecha_en_crudo[14:16])
    new_date = datetime(año, mes,dia,hora,minuto)
    tupla_valores = datetime.isocalendar(new_date)
    #print(año,mes,dia,tupla_valores[2]+1,hora,minuto)
    return [año,mes,dia,tupla_valores[2]+1,hora,minuto]

def gender (sex):
    if sex == 'M':
        sex = 1
    else:
        sex = 0
    return sex

def yesno(answer):
    if answer == 'Yes':
        answer = 1
    else:
        answer = 0
    return answer
