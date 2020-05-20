#importando módulos
import emoji
from  random import randint
from time import sleep

#uma breve conversa antes do jogo começar
nome = input("Olá! Poderia me dizer o seu nome? ")
print("Olá, {}! Quer jogar um pouco comigo?".format(nome))
resposta = str(input("Digite sim ou não: ")).upper()
if resposta == 'NÃO' or resposta == 'NAO':
    print("Que pena! Então até a proxima.")
else:
    print("Ótimo, vamos jogar pedra, papel e tesoura!")
#definindo os itens com emoji e criando um loop para o jogo
    while True:

        itens = ((emoji.emojize(":fist:", use_aliases = True)), (emoji.emojize(":hand:", use_aliases = True)), (emoji.emojize(":v:", use_aliases = True)))
        maquina = randint(0, 2)
        print('''Escolha uma das opções:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA''')
        jogador = int(input("Faça a sua jogada: "))
        if jogador >= 3:
            print("Não existe essa opção, por favor vamos brincar direito!")
            break
        #fazendo a simulação como se estivesse falando real
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!")
        #mostra a escolha da máquina e do jogador
        print('-=' * 11)
        print("Eu escolho {}".format(itens[maquina]))
        print("{} jogou {}".format(nome, itens[jogador]))
        print('-=' * 11 )
        #mostra quem ganhou ou se deu empate
        if maquina == 0: #PEDRA
            if jogador == 0:
                print("EMPATE!")
            elif jogador == 1:
                print("{} VENCEU!".format(nome))
            elif jogador == 2:
                print("EU VENCI!")
        elif maquina == 1:  #PAPEL
            if jogador == 0:
                print("EU VENCI!")
            elif jogador == 1:
                print("EMPATE!")
            elif jogador == 2:
                print("{} VENCEU!".format(nome))
        elif maquina == 2:  #TESOURA
            if jogador == 0:
                print("{} VENCEU!".format(nome))
            elif jogador == 1:
                print("EU VENCI!")
            elif jogador == 2:
                print("EMPATE!")
        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
        #finalizando o jogo ou recomeçando o
        opcao = input("Pressione \'q\' para sair ou digite qualquer letra para jogar: ")
        if opcao == 'Q' or opcao == 'q':
            break    