#O ganho por horas trabalhadas e dias junto com os descontos.

salario_base = float(input("Digite o seu salário bruto: "))
dias = int(input("Digite quantos dias na semana você trabalha: "))
horas = float(input("Digite quantas horas você trabalha diariamente: "))
descontos = salario_base * 14 / 100

def calculadora():
    if horas == 8 and dias == 5:
        diaria = salario_base / 24
        por_hora = diaria / 8
        print('*** Descontos***')
        print('INSS: 8%')
        print('VT: 6%')
        print('Com os descontos o seu salário bruto fica em: R${}'.format(salario_base - descontos))
        print('Você ganha R${:.2f} diariamente e R${:.2f} por horas trabalhadas.'.format(diaria - (diaria * 14 / 100), por_hora - (por_hora * 14 / 100)))
    elif horas == 6 and dias == 6 or dias == 5:
        diaria = salario_base / 26
        por_hora = diaria / 6
        print('*** Descontos***')
        print('INSS: 8%')
        print('VT: 6%')
        print('Com os descontos o seu salário bruto fica em: R${}'.format(salario_base - descontos))
        print('Você ganha R${:.2f} diariamente e R${:.2f} por horas trabalhadas.'.format(diaria - (diaria * 14 / 100), por_hora - (por_hora * 14 / 100)))
    else:
        print('Você digitou um horário ou dia inválido.')
calculadora()
