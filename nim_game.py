def computador_escolhe_jogada(n,m):
    m_original = m
    if m >= n:
            print("Computador removeu", n, "peças.")
            return n
    while m > 0:
        if (n - m) % (m_original + 1) == 0:
            print("Computador removeu", m, "peças.")
            return m
        else:
            m = m - 1
    print("Computador removeu", m_original, "peças.")
    return m_original

def usuario_escolhe_jogada(n,m):
    while True:
        remover = int(input("Quantas peças você vai tirar? "))
        if remover > n:
            print("O tabuleiro só tem", n, "peças e o limite por rodada é", m, "peças.")
        elif remover > m:
            print("Você não pode remover mais que", m, "peças por vez.")
        elif remover <= 0:
            print("Você não pode remover", remover, "peças.")    
        else:
            return remover

def partida():
    n, m = 0, 0
    while n <= 0:
        n = int(input("Quantas peças? "))
        if n <= 0:
            print("Não é possível iniciar o jogo com", n, "peças.")
    while m <= 0:
        m = int(input("Limite de peças por jogada? "))
        if m <= 0:
            print("Não é possível jogar removendo", m, "peças por rodada.")
 
    vez_do_computador = None
    if vez_do_computador == None:
        if n % (m + 1) == 0:
            print("Você começa!")
            vez_do_computador = False
        else:
            print("Computador começa!")
            vez_do_computador = True
    
    while not n == 0:
        if vez_do_computador == True:
            n = n - computador_escolhe_jogada(n,m)
            vez_do_computador = False
            print("Restam", n, "peças")
        else:
            n = n - usuario_escolhe_jogada(n,m)
            vez_do_computador = True
            print("Restam", n, "peças")
    
    if vez_do_computador == True:
        print("Parabéns, você ganhou??? De alguma forma kkkk")
        return True
    if vez_do_computador == False:
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