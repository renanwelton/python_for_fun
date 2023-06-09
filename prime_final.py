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
            print()
            print_prime(num, loop)

        if choice == "3":
            num = ensure_int("Previous and next primes of what number?")
            if prev_prime(num) == False:
                print("\n" + str(num), "has no previous primes. The next is", str(next_prime(num)) + ".")
            else:
                print("\nThe previous prime of", num, "is", str((prev_prime(num))) + '.', "The next is", str(next_prime(num)) + ".")
    
        if choice == "4":
            num_1 = ensure_int("Starting number (default 0):")
            num_2 = ensure_int("Finishing number:")
            primes_count = primes_between(num_1, num_2)
            if primes_count == False:
                print("You typed the same number.")
            elif primes_count == None:
                print("\nThere's no primes between", num_1, "and", str(num_2)+".")
            else:
                print("\nThere's", primes_count, "primes between", num_1, "and", str(num_2)+".\n")
      
        if choice == "5":
            cont = input("\nThis operation will only stop if the program is forcibly closed. Do you want to continue? (Y/n) ")
            if cont in yes:
                num = ensure_int("Starting number (default 0):")
                print_prime(int(num), -1)
    print()
            
def check_prime(num):
    """ Checks if a given number is prime. """
    div = 2
    if num > 0:
        sqrt = math.sqrt(num)
    while True:
        if num % div == 0 and num != 2 or num < 2:
            return False
        div = div + 1
        if div > sqrt or num == 2:
            primes.append(num)
            return True

def print_prime(num, loop):
    """ Prints only prime numbers for a given number of times.
        Passing a negative value to loop causes it to loop indefinitely. """
    while not loop == 0:
        if check_prime(num) == True:
            print(num) 
            loop = loop - 1
        num += 1

def primes_between(num_1, num_2):
    """ Finds out how many primes exist between 2 given numbers, excluding the numbers themselves. """
    print()
    primes_count = 0
    if num_1 == num_2:
        return False
    while num_1 < num_2 - 1:
        num_1 += 1
        if check_prime(num_1) == True:
            primes_count += 1
            print(num_1)
    while num_1 > num_2 + 1:
        num_1 -= 1
        if check_prime(num_1) == True:
            primes_count += 1
            print(num_1)      
    if primes_count == 0:
        return None
    else:
        return primes_count
  
def next_prime(num):
    """ Returns the next prime of a given number """
    while check_prime(num + 1) == False:
        num += 1
    return num + 1

def prev_prime(num):
    """ Returns the previous prime of a given number bigger than 2 """
    if num <= 2:
        return False
    while check_prime(num - 1) == False:
        num -= 1
    return num - 1

def ensure_int(ask):
    """ Works like input(), but ensures the input is an integer. Returns 0 by default. """
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
                print("\nError! Type an integer, please.")

main()