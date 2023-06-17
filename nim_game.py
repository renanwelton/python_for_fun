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

def game_start():
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
    else:
        if random.randint(1,2) == 1:
            computer_turn == False
        else:
            computer_turn == True

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
        print("End of the game! Somehow you won!")
        return True
    if computer_turn == False:
        print("End of the game! Computer won!")
        return False

def main():
    print("\nWecolme to NIM GAME!\n\n1 - To play one match.\n2 - To play championship.\n")
    choice = ensure_int()
    if choice == 1:
        print("Let's play one match then...")
        game_start()
    if choice == 2:
        print("Better out of 3 matches, let's go!")
        games, round = 3, 1
        comp, usr = 0, 0
        while games > 0:
            print("**** Round", round, "****")
            if not game_start():
                comp += 1
            else:
                usr += 1
            games -= 1
            round += 1
        print('You', usr, 'X', comp, 'Computer.')

if __name__ == "__main__":
    main()