#importando módulos
from  random import choice
from time import sleep

#uma breve conversa antes do jogo começar
nome = input("Olá! Poderia me dizer o seu nome? ")
print("Olá, {}! Quer jogar um pouco comigo?".format(nome))
resposta = str(input("Digite sim ou não: ")).upper()
if resposta == 'NÃO' or resposta == 'NAO':
    print("Que pena! Então até a proxima.")
else:
    print("Ótimo, vamos jogar pedra, papel e tesoura!")
    sleep(2)
    while True:
        def empate():
            if maquina == jogador:
                print("DEU EMPATE!")

        def maquinaWins():
            if maquina == "pedra" and jogador == "tesoura" or maquina == "papel" and jogador == "pedra" or maquina == "tesoura" and jogador == "papel":
                print("EU VENCI!")

        def jogadorWins():
            if maquina == "pedra" and jogador == "papel" or maquina == "papel" and jogador == "tesoura" or maquina == "tesoura" and jogador == "pedra":
                print("VOCÊ GANHOU!")

        itens = ("pedra", "papel", "tesoura")
        maquina = choice(itens)
        print('''Escolha uma das opções:
-pedra
-papel
-tesoura''')
        jogador = str(input("Escreva a sua opção: "))
        while jogador != "pedra" and jogador != "papel" and jogador != "tesoura":
            jogador = str(input("Escreva a sua opção: "))
        #fazendo a simulação como se estivesse falando real
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!")
        #mostra a escolha da máquina e do jogador
        print('-=' * 11)
        print("Eu escolho {}".format(maquina))
        print("{} jogou {}".format(nome, jogador))
        print('-=' * 11 )
        #mostra quem ganhou ou se deu empate
        empate()
        maquinaWins()
        jogadorWins()       
        #finalizando o jogo ou recomeçando o
        opcao = input("Pressione \'q\' para sair ou digite qualquer letra para jogar: ")
        if opcao == 'Q' or opcao == 'q':
            break
