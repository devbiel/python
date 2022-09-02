salario_mensal = int(input('Digite o seu salário mensal: '))
indice = int(input('Digite em quantos porcentos o seu salário será alterado: '))
calculo = salario_mensal * (indice / 100)

print('''O seu salário atual é: {}
O índice em porcentagens é de: {}. 
Portanto, o seu novo salário será de: {}.'''.format(salario_mensal, indice, salario_mensal + calculo))
