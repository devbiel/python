print('Aperte 1 para converter (Decimal) para (Binário).')
print('Aperte 2 para converter (Decimal) para (Octal).')
print('Aperte 3 para converter (Decimal) para (Hexa).')
print('Aperte 4 para converter (Hexa) para (Decimal).')
print()
ask = int(input('Digite uma das opções para as conversões.'))
print()
if ask == 1:
    x = int(input('Digite um número para a conversão de (Decimal) para (Binário): '))
    binario = []
    while x > 1:
        resto = x % 2
        print(int(x), "dividido por 2 tem o resto", int(resto))
        x = x / 2
        binario.append(int(resto))
    binario.reverse()
    print('o resultado é: ', *binario, sep='')
        
elif ask == 2:
    x = int(input('Digite um número para a conversão de (Decimal) para (Octal): '))
    octal = []
    while x > 1:
        resto = x % 8
        print(int(x), "dividido por 8 tem o resto", int(resto))
        x = x / 8
        octal.append(int(resto))
    octal.reverse()
    print('o resultado é: ', *octal, sep='')
        
elif ask == 3:
    x = int(input('Digite um número para a conversão de (Decimal) para (Hexa): '))
    hexa = []
    while x > 1:
        resto = x % 16
        print(int(x), "dividido por 16 tem o resto", int(resto))
        x = x / 16
        hexa.append(int(resto))
    hexa.reverse()
    if 10 in hexa:
        conversao_A = hexa.index(10)
        hexa[conversao_A] = 'A'
    elif 11 in hexa:
        conversao_B = hexa.index(11)
        hexa[conversao_B] = 'B'
    elif 12 in hexa:
        conversao_C = hexa.index(12)
        hexa[conversao_C] = 'C'
    elif 13 in hexa:
        conversao_D = hexa.index(13)
        hexa[conversao_D] = 'D'
    elif 14 in hexa:
        conversao_E = hexa.index(14)
        hexa[conversao_E] = 'E'
    elif 15 in hexa:
        conversao_F = hexa.index(15)
        hexa[conversao_F] = 'F'
    print('o resultado é: ', *hexa, sep='')
    
elif ask == 4:
    x = input('Digite os número e letras(EM MAIUSCULO) para a conversão de (Hexa) para (Decimal): ')
    decimal = []
    for i in x:
        decimal.append(i)
        
    if 'A'.lower().upper() in decimal:
        conversao_Hexa = decimal.index('A'.lower().upper())
        decimal[conversao_Hexa] = 10
    if 'B'.lower().upper() in decimal:
        conversao_Hexb = decimal.index('B'.lower().upper())
        decimal[conversao_Hexb] = 11
    if 'C'.lower().upper() in decimal:
        conversao_Hexc = decimal.index('C'.lower().upper())
        decimal[conversao_Hexc] = 12
    if 'D'.lower().upper() in decimal:
        conversao_Hexd = decimal.index('D'.lower().upper())
        decimal[conversao_Hexd] = 13
    if 'E'.lower().upper() in decimal:
        conversao_Hexe = decimal.index('E'.lower().upper())
        decimal[conversao_Hexe] = 14
    elif 'F'.lower().upper() in decimal:
        conversao_Hexf = decimal.index('F'.lower().upper())
        decimal[conversao_Hexf] = 15
    print(decimal)
        
    
else:
    print('Opção errada.')
