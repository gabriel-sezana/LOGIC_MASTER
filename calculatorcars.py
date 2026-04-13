valor_pago = float(input('Digite o valor pago: '))
valor_invest = float(input('Digite o valor gasto: '))
valor_venda = float(input('Digite o valor da venda: '))

custo_total = valor_pago + valor_invest
lucro = valor_venda - custo_total 


if lucro >0:
    print('Resultado: lucro na venda de R$' + str(lucro))

elif lucro == 0:
    print('Resultado: R$' + str(lucro))

else:
    print('Voce teve prejuizo de R$' + str(lucro))
  
          
