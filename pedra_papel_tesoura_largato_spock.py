import random

pedra = 'Pedra', ('Tesoura', 'Lagarto')
papel = 'Papel', ('Pedra', 'Spock')
tesoura = 'Tesoura', ('Lagarto', 'Papel')
lagarto = 'Lagarto', ('Spock', 'Papel')   
spock = 'Spock', ('Tesoura','Pedra')  

lista_jogadas = None, pedra, papel, tesoura, lagarto, spock

jogadas_validas = '1', '2', '3', '4', '5'

def main():
    print('\nVamos jogar Pedra-Papel-Tesoura-Lagarto-Spock?')
    print('\n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Lagarto\n5 - Spock\n')
    usuario_jogou = jogada_usuario()
    computador_jogou = jogada_computador()
    escolhas_jogadores = usuario_jogou[:1] + computador_jogou[:1]
    mensagem_vitoria(escolhas_jogadores)
    if usuario_jogou[0] == computador_jogou[0]:
        print('EMPATE, tente outra vez!')
        main()
    elif usuario_jogou[0] in computador_jogou[1]:
        print('\nCOMPUTADOR VENCEU!\n')
    else:
        print('\nVOCÊ VENCEU!\n')

def jogada_usuario():
    jogada = None
    while not jogada in jogadas_validas:
        jogada = input('Escolha sua jogada: ')
        if not jogada in jogadas_validas:
            print('Digite um valor válido (1-5).')
    jogada = int(jogada)
    print('\nVocê escolheu', lista_jogadas[jogada][0], end='. ')
    return lista_jogadas[jogada]

def jogada_computador():
    jogada = random.randint(1,5)
    print('Computador escolheu', lista_jogadas[jogada][0] + '.\n')
    return lista_jogadas[jogada]

def mensagem_vitoria(escolha_jogadores):
    mensagems = (
    ('Tesoura', 'Papel', 'Tesoura corta Papel'),
    ('Pedra', 'Papel', 'Papel cobre Pedra'),
    ('Lagarto', 'Pedra', 'Pedra esmaga Lagarto'),
    ('Spock', 'Lagarto', 'Largato envenena Spock'),
    ('Tesoura', 'Spock', 'Spock esmaga Tesoura'),
    ('Tesoura', 'Lagarto', 'Tesoura decapita Lagarto'),
    ('Lagarto', 'Papel', 'Lagarto come Papel'),
    ('Spock', 'Papel', 'Papel refuta Spock'),
    ('Pedra', 'Spock', 'Spock vaporiza Pedra'),
    ('Tesoura', 'Pedra', 'Pedra amassa Tesoura'))
    
    for lista in mensagems:
        if escolha_jogadores[0] in lista and escolha_jogadores[1] in lista:
            if escolha_jogadores[0] != escolha_jogadores[1]:
                print(lista[2])

main()