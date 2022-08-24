# Calculadora de Indice de masa corporal
# Formula: peso / (Altura * Altura)
#Resultados:
# < 20 Delgadez, entre 20 y 25 Normal, entre 26 y 30 Sobrepeso, > a 30 Obesidad

peso = int(input('Ingrese su peso en kg '))

altura = float(input('ingrese su altura en metros. Ej: 1.73 '))

imc = peso / (altura * altura)

print('Su IMC es ' + str(imc))

if imc < 20:
    print('Te encuentras en estado de delgadez')
if imc >= 20 and imc < 26:
    print('Te encuentras en un peso normal')
if imc >= 26 and imc <= 30:
    print('Te encuentras en un estado de sobrepeso') 
if imc >= 31:
    print('Te encuentras en un estado de obesidad')   