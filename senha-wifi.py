from os import system

system('cls')

system('netsh wlan show profiles')

nome_rede = input("Digite o nome da rede: ")

senha = 'netsh wlan show profile name="' + nome_rede + '" key=clear'

system(senha)
