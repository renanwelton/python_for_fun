import random

computer_always_wins = True

def ensure_int():
    while True:
        try:
            num = int(input(">>> "))
            return num
        except ValueError:
            print("Kinda hard to play with that, type something else.")

def computer_play(n,m):
    m_original = m
    if m >= n:
            print("Computer removed", n, "pieces.")
            return n
    while m > 0:
        if (n - m) % (m_original + 1) == 0:
            print("Computer removed", m, "pieces.")
            return m
        else:
            m = m - 1
    print("Computer removed", m_original, "pieces.")
    return m_original

def user_play(n,m):
    while True:
        print('How many pieces you want to remove?')
        remove = ensure_int()
        if remove > n:
            print("The board only has", n, "pieces.")
        elif remove > m:
            print("You cannot remove more than", m, "pieces at a time.")
        elif remove <= 0:
            print("You can't remove", remove, "pieces.")    
        else:
            return remove

def partida():
    n, m = 0, 0
    while n <= 0:
        print("Total of pieces on the board: ")
        n = ensure_int()
        if n <= 0:
            print("It's not possible to start the game with", n, "pieces.")
    while m <= 0:
        print("Limit of pieces to be removed at a time:")
        m = ensure_int()
        if m <= 0:
            print("It's not possible to play removing", m, "pieces per turn.")
 
    computer_turn = None

    if computer_turn == None and computer_always_wins == True:
        if n % (m + 1) == 0:
            print("You start!")
            computer_turn = False
        else:
            print("Computer starts!")
            computer_turn = True
    
    while not n == 0:
        if computer_turn == True:
            n = n - computer_play(n,m)
            computer_turn = False
            print( n, "remaining pieces")
        else:
            n = n - user_play(n,m)
            computer_turn = True
            print(n, "remaining pieces")
    
    if computer_turn == True:
        print("Parabéns, você ganhou??? De alguma forma kkkk")
        return True
    if computer_turn == False:
        print("Fim do jogo! O computador ganhou!")
        return False

def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha:\n1 - Para jogar uma partida isolada.\n2 - Para jogar um campeonato.")
    escolha = int(input("Qual a sua escolha? "))
    if escolha == 1:
        print("Você escolheu jogar uma partida!")
        partida()
    if escolha == 2:
        print("Você escolheu campeonato!")
        partidas = 3
        rodada = 1
        computador = 0
        usuario = 0
        while partidas > 0:
            print("**** Rodada", rodada, "****")
            if partida() == False:
                computador = computador + 1
            else:
                usuario = usuario + 1
            partidas = partidas - 1
            rodada = rodada + 1
        print('Placar: Você', usuario, 'X', computador, 'Computador.')

campeonato()