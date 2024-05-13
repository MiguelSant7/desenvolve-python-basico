#Questao4 - Horas (datatime)

#Bibliotecas
import datetime

data_hora = datetime.datetime.now()
data_f    = data_hora.strftime("%d/%m/%Y")
hora_f    = data_hora.strftime("%H:%M")

print("Data:", data_f)
print("Hora:", hora_f)
