import random

rock = ['Rock', ['Scissors', 'Lizard']]
paper = ['Paper', ['Rock', 'Spock']]
scissors = ['Scissors', ['Lizard', 'Paper']]
lizard = ['Lizard', ['Spock', 'Paper']]  
spock = ['Spock', ['Scissors','Rocks']]  

# None is here just to fix the index
list_plays = None, rock, paper, scissors, lizard, spock

valid_plays= ['1', '2', '3', '4', '5']

def main():
    print("\nLet's play Rock-Paper-Scissors-Lizard-Spock?")
    print('\n1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n')
    user_played = user_play()
    comp_played = comp_play()
    plays_from_usr_comp = user_played[:1] + comp_played[:1]
    if user_played[0] is comp_played[0]:
        print('DRAW, try again!')
        main()
    else:
        victory_msm(plays_from_usr_comp) 
        if user_played[0] in comp_played[1]:
            print('\nCOMPUTER WON!\n')
        else:
            print('\nYOU WON!\n')

def user_play():
    play = None
    while not play in valid_plays:
        play = input('Your play: ')
        if not play in valid_plays:
            print('Type a valid value (1-5).')
    play = int(play)
    print('\nYou chose', list_plays[play][0], end='. ')
    return list_plays[play]

def comp_play():
    play = random.randint(1,5)
    print('Computer chose', list_plays[play][0] + '.\n')
    return list_plays[play]

def victory_msm(plays_from_usr_comp):
    win_text = [
        ['Scissors', 'Paper', ['Scissors cuts Paper']],
        ['Rock', 'Paper', ['Paper covers Rock']],
        ['Lizard', 'Rock', ['Rock crushes Lizard']],
        ['Spock', 'Lizard', ['Lizard poisons Spock']],
        ['Scissors', 'Spock', ['Spock smashes Scissors']],
        ['Scissors', 'Lizard', ['Scissors decapitates Lizard']],
        ['Lizard', 'Paper', ['Lizard eats Paper']],
        ['Spock', 'Paper', ['Paper disproves Spock']],
        ['Rock', 'Spock', ['Spock vaporizes Rock']],
        ['Scissors', 'Rock', ['Rock crushes Scissors']]
    ]
        
    for list in win_text:
        if plays_from_usr_comp[0] in list and plays_from_usr_comp[1] in list:
            print(list[2][0])
            break

main()