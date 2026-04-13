peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)
imc = round(imc,2)
print('Seu imc é ' + str(imc))

"""
Abaixo de 18,5 → Abaixo do peso
18,5 a 24,9 → Peso normal
25 a 29,9 → Sobrepeso
30 a 34,9 → Obesidade grau I
35 a 39,9 → Obesidade grau II
40+ → Obesidade grau III

"""

if imc < 18.5:
    print('Abaixo do peso')

elif imc >=18.5 and imc <=24.9:
    print('Peso normal')

elif imc >=25 and imc <= 29.9:
    print('Sobrepeso')

elif imc >=30 and imc <= 34.9:
    print('Obesidade grau I')

elif imc >=35 and imc <= 39.9:
    print('Obesidade grau II')

else:
    print('Obesidade grau III')


