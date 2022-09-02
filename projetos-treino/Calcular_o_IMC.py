altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
divisao = int(altura * altura)
imc = peso / divisao
print('O indice de massa corporal ideal para você é: {:.5f}'.format(imc))
