#imported libs
from IPython.display import clear_output

def telaInicial():
    print("+======================+")
    print("+      Tic-Tac-Toe     +")
    print("+======================+\n")
    print("   O   | X   X |       ")
    print(" O   O |   X   |       ")
    print("   O   | X   X |       ")
    print("-------+-------+-------")
    print("       | X   X |   O   ")
    print("       |   X   | O   O ")
    print("       | X   X |   O   ")
    print("-------+-------+-------")
    print(" X   X |       |   O   ")
    print("   X   |       | O   O ")
    print(" X   X |       |   O   ")

def jogoInit():
    return ["","","","","","","","",""]

def numJogos():
    return int(input("\nQuantas partidas deseja jogar?\n"))

def telaReplay():
    if input("\nDeseja jogar outra rodada? (s/n)\n") == 's':
        return True
    else:
        return False

def nomeJogadores(num):
    nome = input(f"\nQual o nome do jogador {num}?\n")
    
    if nome != "":
        return nome

    return "Player "+num
    
def processaJogada(numJogador, jogo):
    #se tile ocupada, retornar mensagem
    posJogada = 0

    while True:
        posJogada = input(f"Qual posição deseja jogar(1~9):\n")
        if posJogada == "help":
            printaLegenda()
        elif posJogada == "jogo":
            printaJogo(jogo)
        elif int(posJogada) in range(0,10):
            #confere posicao disponível
            posJogada = int(posJogada)

            if jogo[posJogada-1] == "":
                jogo[posJogada-1] = "x" if numJogador == 1 else "o"
                return jogo
            else:
                print("Já está ocupado! Tente outro espaço.\n")

        else:
            print("Jogada inválida! Tente novamente.\n")

def printaLegenda():
    print("==Legenda==")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

def printaJogo(jogo):
    #Elementos básicos
    circle = {0:"   O   |",1:" O   O |"}
    cross = {0:" X   X |",1:"   X   |"}
    vazio = "       |"
    divisoria = "-------+-------+-------:\n"
    #Inicializacao Tela Jogo
    telaJogo = ""

    #Construcao Tela Jogo
    for i in range(0,7,3):
        for j in range(0,3):
            for k in range(0,3):
                if jogo[k+i] == "o":
                    telaJogo +=circle[j%2]
                elif jogo[k+i] == "x":
                    telaJogo +=cross[j%2]
                else:
                    telaJogo +=vazio
            telaJogo +="\n"
        telaJogo += divisoria
    print(telaJogo)

def jogoAcabou(jogo, vezJogador1):
    numConsec = 0
    tic = ""

    if vezJogador1:
        tic = "x"
    else:
        tic = "o"

    #TESTE VITORIA
    #teste horizontal
    for i in range(0,7,3):
        for k in range(0,3):
            if jogo[i+k] == tic:
                numConsec += 1
            else:
                numConsec = 0
            if numConsec == 3:
                return "vitoria"
                
    #teste vertical
    for i in range(0,3):
        for k in range(0,7,3):
            if jogo[i+k] == tic:
                numConsec += 1
            else:
                numConsec = 0
            if numConsec == 3:
                return "vitoria"

    #teste diagonal
    for i in range(0,9,4):
        if jogo[i] == tic:
            numConsec += 1
        else:
            numConsec = 0
        if numConsec == 3:
            return "vitoria"

    for i in range(2,7,2):
        if jogo[i] == tic:
            numConsec += 1
        else:
            numConsec = 0
        if numConsec == 3:
            return "vitoria"

    #Confere se todos os espaços foram preenchidos
    for x in jogo:
        if x == "":
            return "nao"

    #acabou jogadas, masm ninguém venceu
    return "empate"

def mostraScore(score):
    print("+" +"="*int(len(jogador1)+len(jogador2)+5)+"+")
    print("|"+" "*int((len(jogador1)+len(jogador2))/2)+ "Score"+" "*int((len(jogador1)+len(jogador2))/2)+ " |")
    print("+" +"="*int(len(jogador1)+len(jogador2)+5)+"+")
    print("| "+jogador1 + " | "+jogador2+" |")
    print(("|"+" "*int((len(jogador1)+len(jogador2))/4+1)+ "{}" +" "*int((len(jogador1)+len(jogador2))/4)+ " | "+" "*int((len(jogador1)+len(jogador2))/4)+ "{}"+" "*int((len(jogador1)+len(jogador2))/4)+ "|").format(score[0],score[1]))
    print("+" +"="*int(len(jogador1)+len(jogador2)+5)+"+")

def mostraCampeao(jogador):
    print("+======================+")
    print("+======================+")
    print("         CAMPEAO        ")
    print("       "+jogador+"       ")
    print("+======================+")
    print("+======================+\n")

##============== JOGO ===================
#Init variables
score = [0,0]
numPartidas = 1
jogador1 = ""
jogador2 = ""
jogo = []
replay = True
vezJogador1 = False
fimJogo = "nao"

#Printa tela inicial
telaInicial()

while replay:
    
    #Nome Jogadores
    jogador1 = nomeJogadores(1)
    jogador2 = nomeJogadores(2)
    
    #Numero Partidas
    numPartidas = numJogos()
    
    while numPartidas > 0:
        jogo = jogoInit()
        while fimJogo == "nao":
            vezJogador1 = not(vezJogador1)
            printaJogo(jogo)
            printaLegenda()
            
            if vezJogador1:
                print(f"SUA VEZ {jogador1}")
            else:
                print(f"SUA VEZ {jogador2}")

            jogo = processaJogada(vezJogador1, jogo)
            fimJogo = jogoAcabou(jogo,vezJogador1)
            clear_output()


        if fimJogo == "empate":
            print("JOGO DA VELHA!!!! NINGUEM PONTUOU!!")
            printaJogo(jogo)
        else:
            printaJogo(jogo)
            if vezJogador1:
                print(f"VITORA DE {jogador1}")
                score[0]+=1
            else:
                print(f"VITORA DE {jogador2}")
                score[1]+=1
        
        fimJogo = "nao"
        numPartidas -= 1   
        mostraScore(score)
    
    if score[0] > score[1]:
        mostraCampeao(jogador1)
    elif score[0] > score[1]:
        mostraCampeao(jogador2)
    else:
        print("DEU EMPATE")
    replay = telaReplay()
