## tell in operation 3 and 4 if the input is also prime

import math

options = ["1", "2", "3", "4", "5"]
yes = ["Yes", "yes", "Y", "y", ""]

def main():
    print("\n --- WELCOME TO MY PROGRAM ---\n")
    print("1 - Check if given number is prime.")
    print("2 - Print set amount of primes.")
    print("3 - Print next and previous primes of given number.")
    print("4 - Print all primes between two numbers")
    print("5 - Generate primes indefinitely from any starting point.\n")
    print("To exit press anything else.\n")
    
    choice = (input("Choose operation: "))

    if choice in options:
        
        if choice == "1":
            num = ensure_int("What number do you want to check?")
            if check_prime(num) == True:
                print("\nYes,", num, "is prime.")
            else:
                print("\nNo,", num, "is not prime.")
                
        if choice == "2":
            num = ensure_int("Starting number (default 0):")
            loop = ensure_int("How many primes do you want to print?")
            if loop <= 0:
                print("\nWell, see you later!")
            else:
                print()
                print_prime(num, loop)

        if choice == "3":
            num = ensure_int("Previous and next primes of what number?")
            if prev_prime(num) == False:
                print("\n" + num, "has no previous primes. The next is", str(next_prime(num)) + ".")
            else:
                print("\n" + "The previous prime of", num, "is", str((prev_prime(num))) + '.', "The next is", str(next_prime(num)) + ".")
    
        if choice == "4":
            num1 = ensure_int("Starting number (default 0):")
            num2 = ensure_int("Finishing number:")
            primes = primes_between(num1, num2)
            if primes == False:
                print("\nYou typed the same number.")
            elif primes == None:
                print("\nThere's no primes between", num1, "and", str(num2)+".")
            else:
                print("\nThere's", len(primes), "primes between", num1, "and", str(num2)+".\n")
                for prime in primes:
                    print(prime)
      
        if choice == "5":
            cont = input("\nThis operation will only stop if the program is forcibly closed. Do you want to continue? (Y/n) ")
            if cont in yes:
                num = ensure_int("Starting number (default 0):")
                print_prime(int(num), -1)
    print()
            
def check_prime(num):
    div = 2
    if num > 0:
        sqrt = math.sqrt(num)
    while True:
        if num % div == 0 and num != 2 or num < 2:
            return False
        div = div + 1
        if div > sqrt or num == 2:
            return True

def print_prime(num, loop): ## Passing a negative value to loop causes it to loop indefinitely ##
    while not loop == 0:
        if check_prime(num) == True:
            print(num) 
            loop = loop - 1
        num += 1

def primes_between(num1, num2): ## heavy rewrite need! 
    if num1 == num2:
        return False
    primes = []
    while num1 < num2 - 1:
        num1 = num1 + 1
        if check_prime(num1) == True:
            primes.append(num1)
    while num1 > num2 + 1:
        num1 = num1 - 1
        if check_prime(num1) == True:
            primes.append(num1)
    if len(primes) == 0:
        return None
    else:
        return primes
      
def next_prime(num):
    num += 1
    while check_prime(num) == False:
        num += 1
    return num 

def prev_prime(num):
    if num <= 2:
        return False
    num -= 1
    while check_prime(num) == False:
        num -= 1
    return num

def ensure_int(ask):
    while True:
        print("\n" + ask, end = " ")
        num = input()
        if num in [""]:
            return 0
        else:
            try:
                num = int(num)
                return num
            except ValueError:
                print("\nYou must type an integer!")

main()