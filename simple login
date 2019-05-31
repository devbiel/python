#This is a simple login

acc = {'user':'', 'pass':''}
for i in range(1):
    print('*'*20 )
    print("Criação da conta")
    print('*'*20 )

createuser = input('Digite um nome de usuário: ')
createpass = input("Digite uma senha: ")

acc['user'] = createuser
acc['pass'] = createpass
print("\tConta criada com Sucesso!")

choice = input("Digite 'Y' para digitar novamente, ou 'N' para sair.")

if choice.upper().lower() == 'y':
    user = input("Digite o seu Usuário para logar: ")
    passw = input("Digite a sua senha: ")
    if user == acc['user'] and passw == acc['pass']:
        print("\tLogado com sucesso!")
        #Change password
        ask = input("\tVocê quer trocar a sua senha? 'Y' para sim ou 'N' para não.")
        if ask.upper().lower() == 'y':
            newpass = input('\tDigite a sua nova senha: ')
            print('\tSenha antiga:', acc['pass'])
            acc['pass'] = newpass
            print('\tSua nova senha é:', acc['pass'])
        else:
            print("Okay")
    else:
        print("Usuário ou senha incorreto!")
elif choice.upper().lower():
    print("Fim.")
else:
    print("Opção inválida")
