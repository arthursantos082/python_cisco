from random import randrange

def exibir_tabuleiro(tabuleiro):
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|       " * 3, "|", sep="")
        for coluna in range(3):
            print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def jogada_usuario(tabuleiro):
    valido = False
    while not valido:
        movimento = input("Digite seu movimento: ")
        valido = len(movimento) == 1 and movimento >= '1' and movimento <= '9'
        if not valido:
            print("Jogada inválida – tente novamente!")
            continue
        movimento = int(movimento) - 1
        linha = movimento // 3
        coluna = movimento % 3
        simbolo = tabuleiro[linha][coluna]
        valido = simbolo not in ['O', 'X']
        if not valido:
            print("Campo já ocupado – tente novamente!")
            continue
    tabuleiro[linha][coluna] = 'O'

def lista_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ['O', 'X']:
                livres.append((linha, coluna))
    return livres

def vitoria(tabuleiro, simbolo):
    if simbolo == "X":
        vencedor = 'computador'
    elif simbolo == "O":
        vencedor = 'jogador'
    else:
        vencedor = None
    diagonal1 = diagonal2 = True
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return vencedor
        if tabuleiro[0][i] == simbolo and tabuleiro[1][i] == simbolo and tabuleiro[2][i] == simbolo:
            return vencedor
        if tabuleiro[i][i] != simbolo:
            diagonal1 = False
        if tabuleiro[2 - i][2 - i] != simbolo:
            diagonal2 = False
    if diagonal1 or diagonal2:
        return vencedor
    return None

def jogada_computador(tabuleiro):
    livres = lista_campos_livres(tabuleiro)
    qtd = len(livres)
    if qtd > 0:
        escolha = randrange(qtd)
        linha, coluna = livres[escolha]
        tabuleiro[linha][coluna] = 'X'

tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = 'X'
livres = lista_campos_livres(tabuleiro)
turno_jogador = True

while len(livres):
    exibir_tabuleiro(tabuleiro)
    if turno_jogador:
        jogada_usuario(tabuleiro)
        vencedor = vitoria(tabuleiro, 'O')
    else:
        jogada_computador(tabuleiro)
        vencedor = vitoria(tabuleiro, 'X')
    if vencedor is not None:
        break
    turno_jogador = not turno_jogador
    livres = lista_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == 'jogador':
    print("Você venceu!")
elif vencedor == 'computador':
    print("O computador venceu!")
else:
    print("Empate!")
from random import randrange

def exibir_tabuleiro(tabuleiro):
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|       " * 3, "|", sep="")
        for coluna in range(3):
            print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def jogada_usuario(tabuleiro):
    valido = False
    while not valido:
        movimento = input("Digite seu movimento: ")
        valido = len(movimento) == 1 and movimento >= '1' and movimento <= '9'
        if not valido:
            print("Jogada inválida – tente novamente!")
            continue
        movimento = int(movimento) - 1
        linha = movimento // 3
        coluna = movimento % 3
        simbolo = tabuleiro[linha][coluna]
        valido = simbolo not in ['O', 'X']
        if not valido:
            print("Campo já ocupado – tente novamente!")
            continue
    tabuleiro[linha][coluna] = 'O'

def lista_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ['O', 'X']:
                livres.append((linha, coluna))
    return livres

def vitoria(tabuleiro, simbolo):
    if simbolo == "X":
        vencedor = 'computador'
    elif simbolo == "O":
        vencedor = 'jogador'
    else:
        vencedor = None
    diagonal1 = diagonal2 = True
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return vencedor
        if tabuleiro[0][i] == simbolo and tabuleiro[1][i] == simbolo and tabuleiro[2][i] == simbolo:
            return vencedor
        if tabuleiro[i][i] != simbolo:
            diagonal1 = False
        if tabuleiro[2 - i][2 - i] != simbolo:
            diagonal2 = False
    if diagonal1 or diagonal2:
        return vencedor
    return None

def jogada_computador(tabuleiro):
    livres = lista_campos_livres(tabuleiro)
    qtd = len(livres)
    if qtd > 0:
        escolha = randrange(qtd)
        linha, coluna = livres[escolha]
        tabuleiro[linha][coluna] = 'X'

tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = 'X'
livres = lista_campos_livres(tabuleiro)
turno_jogador = True

while len(livres):
    exibir_tabuleiro(tabuleiro)
    if turno_jogador:
        jogada_usuario(tabuleiro)
        vencedor = vitoria(tabuleiro, 'O')
    else:
        jogada_computador(tabuleiro)
        vencedor = vitoria(tabuleiro, 'X')
    if vencedor is not None:
        break
    turno_jogador = not turno_jogador
    livres = lista_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == 'jogador':
    print("Você venceu!")
elif vencedor == 'computador':
    print("O computador venceu!")
else:
    print("Empate!")
