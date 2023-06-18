import math
import time
import os

operations_choices = ("1", "2", "3", "4", "5")
yes_all_poss = ("Yes", "yes", "Y", "y", "")

def menu():
    print("\n --- WELCOME TO MY PROGRAM ---\n")
    print("1 - Check if given number is prime.")
    print("2 - Print set amount of primes.")
    print("3 - Print next and previous primes of given number.")
    print("4 - Find how many primes exists between two numbers")
    print("5 - Generate primes indefinitely from any starting point.\n")
    print("To exit press anything else.\n")

    choice = (input("Choose operation: "))

    if choice in operations_choices:

        if choice == "1":
            num = ensure_int("What number do you want to check?")
            if check_prime(num) == True:
                print(f"\nYes, {num} is prime.")
            else:
                print(f"\nNo, {num} is not prime.")
                
        if choice == "2":
            num = ensure_int("Starting number(0):")
            loop = ensure_int("How many primes do you want to print?")
            print()
            print_prime(num, loop)

        if choice == "3":
            num = ensure_int("Previous and next primes of what number?")
            if prev_prime(num) == False:
                print(f"\n{num} has no previous primes. The next is {next_prime(num)}.")
            else:
                print(f"\nThe previous prime of {num} is {prev_prime(num)}. The next is {next_prime(num)}.")
    
        if choice == "4":
            num_1 = ensure_int("Starting number(0):")
            num_2 = ensure_int("Finishing number:")
            primes_count = primes_between(num_1, num_2)
            if primes_count == False:
                print("You typed the same number.")
            elif primes_count == None:
                print(f"\nThere's no primes between {num_1} and {num_2}.")
            else:
                print(f"\nThere's {len(primes_count)} primes between {num_1} and {num_2}.")
                if input("\nDo you want to print them? (Y/n) ") in yes_all_poss:
                    list_print_format(primes_count)
      
        if choice == "5":
            cont = input("\nThis operation will only stop if you press CTRL + C. Do you want to continue? (Y/n) ")
            if cont in yes_all_poss:
                num = ensure_int("Starting number(0):")
                gen_primes_nonstop(num)
        print()
    else:
        return False
            
def check_prime(num):
    """ Checks if a given number is prime. 
        Returns correct value even for negative integers. """
    div = 2
    sqrt = math.sqrt(num)
    while True:
        if num < 2 or (num % div == 0 and num != 2):
            return False
        div = div + 1
        if div > sqrt or num == 2:
            return True

def print_prime(num, loop):
    """ Only prints prime numbers up to n times.
        Passing a negative value to loop causes it to loop indefinitely. """
    while not loop == 0:
        if check_prime(num) == True:
            print(num) 
            loop = loop - 1
        num += 1

def primes_between(num_1, num_2):
    """ Finds out how many primes exist between 2 given numbers. 
        Excludes the numbers themselves. """
    print("\nDon't worry in case you are stuck here, some calculations are being done.")
    primes_count = []
    if num_1 == num_2:
        return False
    
    while num_1 < num_2 - 1:
        num_1 += 1
        if check_prime(num_1):
            primes_count.append(num_1)

    while num_1 > num_2 + 1:
        num_1 -= 1
        if check_prime(num_1):
            primes_count.append(num_2)   

    if len(primes_count) == 0:
        return None
    else:
        return primes_count
  
def next_prime(num):
    """ Returns the next prime of a given number """
    while not check_prime(num + 1):
        num += 1
    return num + 1

def prev_prime(num):
    """ Returns the previous prime of a given number bigger than 2 """
    if num <= 2:
        return False
    while not check_prime(num - 1):
        num -= 1
    return num - 1

def ensure_int(ask):
    """ Works like input(), but ensures the input is an integer.
        Returns 0 by default. """
    while True:
        print(f"\n{ask}", end=" ")
        num = input()
        if num in [""]:
            return 0
        try:
            num = int(num)
            return num
        except ValueError:
            print("\nError! Type an integer, please.")

def gen_primes_nonstop(num):
    """ Handles Keyboard Interruption to stop option 5 and not exit the program. """
    while True:
        try:
            print_prime(num, -1)
        except KeyboardInterrupt:
            time.sleep(1)
            print("\nYou did the right thing, don't worry.")
            break

def list_print_format(list):
    """ Prints every element in a list separating them by a comma.
        The last element is printed with a dot. """
    print()
    for item in list:
        if item == list[-1]:
            print(item, end=".")
        else:
            print(item, end=", ")
    print()

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main():
    while True:

        if not menu() == False:
            print("Press ENTER to go back to MENU. Anything else to EXIT.", end =" ")
        else:
            clear()
            break

        if input() in yes_all_poss:
            time.sleep(1)
            continue
        else:
            clear()
            break

if __name__ == "__main__":
    main()