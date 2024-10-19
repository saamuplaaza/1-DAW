import datetime

hora=datetime.datetime.now().hour
horaRestante=24-int(hora)
minutos=datetime.datetime.now().minute
minutosRestantes=60-int(minutos)

print("Son las %s:%s y te quedan %s horas y %s minutos para que acabe el día."%(hora,minutos,horaRestante,minutosRestantes))