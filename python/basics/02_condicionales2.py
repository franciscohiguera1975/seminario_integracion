"""
Sistema que pida pago por hora y horas trabajadas.
Las primeras 40h son normales, las extras se pagan al 150% 
Calcula y muestra el total semanal
"""

pago_hora = float(input("Pago por Hora"))
horas = float(input("Horas trabajadas esta semana"))
normales = 40*pago_hora
if (horas>40):
    extras=(horas-40)*pago_hora*1.5
    total=normales+extras
else:
    total=normales
print(f"Total a pagar  ${total:.f}")
