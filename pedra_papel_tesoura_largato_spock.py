import random

pedra =   ['Pedra',   ['Tesoura', 'Lagarto']]
papel =   ['Papel',   ['Pedra', 'Spock'    ]]
tesoura = ['Tesoura', ['Lagarto', 'Papel'  ]]
lagarto = ['Lagarto', ['Spock', 'Papel'    ]]
spock =   ['Spock',   ['Tesoura', 'Pedra'  ]]

lista_jogadas = [None, pedra, papel, tesoura, lagarto, spock]
jogadas_validas = ['1', '2', '3', '4', '5']

def menu():
    print()
    print('Vamos jogar Pedra-Papel-Tesoura-Lagarto-Spock?')
    print()
    lista_opcoes = ['1 - Pedra', '2 - Papel', '3 - Tesoura', '4 - Lagarto', '5 - Spock']
    for item in lista_opcoes:
        print(item)

def main():
    print()
    usuario_jogou = jogada_usuario()
    computador_jogou = jogada_computador()
    escolhas_jogadores = usuario_jogou[:1] + computador_jogou[:1]
    mensagem_vitoria(escolhas_jogadores)
    if usuario_jogou[0] is computador_jogou[0]:
        print('Empate, tente outra vez!')
        main()
    elif usuario_jogou[0] in computador_jogou[1]:
        print('Computador venceu!')
    else:
        print('Você venceu!')
    print()

def jogada_usuario():
    jogada = None
    while not jogada in jogadas_validas:
        jogada = input('Escolha sua jogada: ')
        if not jogada in jogadas_validas:
            print('Digite um valor válido (1-5).')
    jogada = int(jogada)
    print()
    print('Você escolheu', lista_jogadas[jogada][0])
    return lista_jogadas[jogada]

def jogada_computador():
    jogada = random.randint(1,5)
    print('Computador escolheu', lista_jogadas[jogada][0])
    return lista_jogadas[jogada]

def mensagem_vitoria(escolha_jogadores):
    mensagems = [
    ['Tesoura', 'Papel', 'Tesoura corta Papel'],
    ['Pedra', 'Papel', 'Papel cobre Pedra'],
    ['Lagarto', 'Pedra', 'Pedra esmaga Lagarto'],
    ['Spock', 'Lagarto', 'Largato envenena Spock'],
    ['Tesoura', 'Spock', 'Spock esmaga Tesoura'],
    ['Tesoura', 'Lagarto', 'Tesoura decapita Lagarto'],
    ['Lagarto', 'Papel', 'Lagarto come Papel'],
    ['Spock', 'Papel', 'Papel refuta Spock'],
    ['Pedra', 'Spock', 'Spock vaporiza Pedra'],
    ['Tesoura', 'Pedra', 'Pedra amassa Tesoura']
]
    for lista in mensagems:
        if escolha_jogadores[0] in lista and escolha_jogadores[1] in lista:
            if escolha_jogadores[0] != escolha_jogadores[1]:
                print(lista[2])

menu()
main()