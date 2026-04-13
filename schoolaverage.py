nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))

soma = nota_1 + nota_2 + nota_3

media = (soma) / 3
media = round(media,2)

if media >=7:
    print('APROVADO!')

elif media >=5:
    print('RECUPERAÇÃO!')

else:
    print('REPROVADO!')


print('Média final: ' + str(media))