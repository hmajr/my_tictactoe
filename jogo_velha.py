def main():
    #Init variables
    replay = True
    score = [0,0]
    numPartidas = 1
    jogador1 = ""
    jogador2 = ""

    #Printa tela inicial
    telaInicial()
    
    #Nome Jogadores
    jogador1 = nomeJogadores(1)
    jogador2 = nomeJogadores(2)

    #Numero partidas

    # #Seleciona
    # while replay:
    # 	score = [0,0]
    #     while numPartidas > 0:

            

def telaInicial():
    print("+======================+")
    print("+      Tic-Tac-Toe     +")
    print("+======================+\n\n")
    print("   O   | X   X |       ")
    print(" O   O |   X   |       ")
    print("   O   | X   X |       ")
    print("-------+---------------")
    print("       |       |       ")
    print("       |       |       ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("       |       |       ")
    print("       |       |       ")

def modoJogo():
    return input("Quantas partidas deseja jogar?")

def telaReplay():
    return input("Deseja jogar outra rodada?")

def nomeJogadores(num):
    nome = input(f"Qual o nome do jogador {num}?")

    if nome != "":
		return nome
	else:
		return "Player "+num
    return 
    
def processaJogada(position, jogador):
    #se tile ocupada, retornar mensagem

def (self, parameter_list):
    pass

