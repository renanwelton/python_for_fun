import math

options = ["1", "2", "3", "4", "5"]
yes = ["Yes", "yes", "Y", "y", ""]

def main():
    print()
    print("1 - Check if a given number is prime.")
    print("2 - Print set amount of primes.")
    print("3 - Print next and previous primes of given number.")
    print("4 - Print all primes between two numbers")
    print("5 - Generate primes indefinitely from any starting point.")
    print()
    print("To exit press anything else.")
    print()
    
    choose = (input("Choose operation: "))
    print()

    if choose in options:
        
        if choose == "1":
            num = int(input("What number do you want to check? "))
            print()
            if prime_check(num) == True:
                print("Yes,", num, "is prime.")
                print()
            else:
                print("No,", num, "is not prime.")
                print()
                
        if choose == "2":
            num = input("Starting number (default = 0): ")
            if num in [""]:
                num = 0
                print()
            else:
                num = int(num)
            loop = int(input("How many primes do you want to print? "))
            if loop <= 0:
                print()
                print("Well, see you later!")
                print()
            else:  
                print()
                print_prime(num, loop)
                print()

        if choose == "3":
            num = int(input("Previous and next primes of what number? "))
            print()
            if num <= 2:
                print(num, "has no previous primes. The next is", next_prime(num))
            else:
                print("The previous prime of", num, "is", str(prev_prime(num)) + ".", "The next is", next_prime(num))
            print()
    
        if choose == "4":
            num1 = int(input("Starting number: "))
            num2 = int(input("Finishing number: "))
            print()
            primes = primes_between(num1, num2)
            if primes == False:
                print("You typed the same number.")
            elif primes == True:
                print("There's primes between", num1, "and", str(num2)+".")
            else:
                print()
                print("There's", primes, "primes between", num1, "and", str(num2)+".")
            print()
      
        if choose == "5":
            cont = input("This operation will only stop if the program is forcibly closed. Do you want to continue? (Y/n) ")
            print()
            if cont in yes:
                num = input("Starting number (default = 0): ")
                if num in [""]:
                    num = 0
                print()
                print_prime(int(num), -1)
            
def prime_check(num):
    div = 2
    if num >= 0:
        sqrt = math.sqrt(num)
    while True:
        if num % div == 0 and num != 2 or num < 2:
            return False
        else:
            div = div + 1
            if div > sqrt or num == 2:
                return True

def print_prime(num, loop): ## passing a negative value to loop causes it to loop indefinitely ##
    while not loop == 0:
        if prime_check(num) == True:
            print(num) 
            loop = loop - 1
        num = num + 1

def primes_between(num1, num2):
    if num1 == num2:
        return False
    else:
        primes = 0
        while num1 < num2 - 1:
            num1 = num1 + 1
            if prime_check(num1) == True:
                print(num1)
                primes = primes + 1
        while num1 > num2 + 1:
            num1 = num1 - 1
            if prime_check(num1) == True:
                print(num1)
                primes = primes + 1
        if primes == 0:
            return True
        else:
            return primes
        
def next_prime(num):
    while prime_check(num + 1) == False:
        num = num + 1
    return num + 1

def prev_prime(num):
    if num <= 2:
        return False
    while prime_check(num - 1) == False:
        num = num - 1
    return num - 1

main()