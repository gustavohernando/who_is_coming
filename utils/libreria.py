from datetime import date
from datetime import datetime

def transformacion(fecha_en_crudo):#dd/mm/aaaa --:--
    dia=int(fecha_en_crudo[:2])
    mes=int(fecha_en_crudo[3:5])
    año=int(fecha_en_crudo[6:10])
    hora=int(fecha_en_crudo[11:13])
    minuto=int(fecha_en_crudo[14:16])
    new_date = datetime(año, mes,dia,hora,minuto)
    tupla_valores = datetime.isocalendar(new_date)
    return [año,mes,tupla_valores[2]+1,hora,minuto]
