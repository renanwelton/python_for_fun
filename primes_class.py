import math
import time
import os


class Primes:
    def prime_check(num):
        """ Checks if a given number is prime. 
            Returns correct value even for negative integers. """
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        sqrt = int(math.sqrt(num))
        for d in range(3, sqrt+1, 2):
            if num % d == 0:
                return False
        return True

    def prime_print(num, loop):
        """ Only prints prime numbers up to n times.
            Passing a negative value to loop causes it to loop indefinitely. """
        while not loop == 0:
            if Primes.prime_check(num) == True:
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
            if Primes.prime_check(num_1):
                primes_count.append(num_1)

        while num_1 > num_2 + 1:
            num_1 -= 1
            if Primes.prime_check(num_1):
                primes_count.append(num_2)   

        if len(primes_count) == 0:
            return None
        else:
            return primes_count
    
    def prime_next(num):
        """ Returns the next prime of a given number """
        while not Primes.prime_check(num + 1):
            num += 1
        return num + 1

    def prime_prev(num):
        """ Returns the previous prime of a given number bigger than 2 """
        if num <= 2:
            return False
        while not Primes.prime_check(num - 1):
            num -= 1
        return num - 1
    
    
class AddFeatures:
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

    def kb_inter_handle(func, *args):
        """ Handles Keyboard Interruption. Receives a function and it's arguments separately. """
        try:
            func(*args)
        except KeyboardInterrupt:
            time.sleep(1)
            print("\nYou did the right thing, don't worry.")

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
            os.system('cls')
        else:
            os.system('clear')


class MainProgram:
    operations_choices = ("1", "2", "3", "4", "5")
    yes_all_poss = ("Yes", "yes", "Y", "y", "")

    def menu():
        print("\n --- WELCOME TO MY PROGRAM ---\n")
        print("1 - Check if given number is prime.")
        print("2 - Print set amount of primes.")
        print("3 - Print next and previous primes of a number.")
        print("4 - Find primes between two numbers")
        print("5 - Generate primes indefinitely.\n")
        print("To exit press anything else.\n")

        choice = (input("Choose operation: "))

        if choice in MainProgram.operations_choices:

            if choice == "1":
                num = AddFeatures.ensure_int("What number do you want to check?")
                if Primes.prime_check(num) == True:
                    print(f"\nYes, {num} is prime.")
                else:
                    print(f"\nNo, {num} is not prime.")
                    
            if choice == "2":
                num = AddFeatures.ensure_int("Starting number(0):")
                loop = AddFeatures.ensure_int("How many primes do you want to print?")
                print()
                Primes.prime_print(num, loop)

            if choice == "3":
                num = AddFeatures.ensure_int("Previous and next primes of what number?")
                if Primes.prime_prev(num) == False:
                    print(f"\n{num} has no previous primes. The next is {Primes.prime_next(num)}.")
                else:
                    print(f"\nThe previous prime of {num} is {Primes.prime_prev(num)}. The next is {Primes.prime_next(num)}.")
        
            if choice == "4":
                num_1 = AddFeatures.ensure_int("Starting number(0):")
                num_2 = AddFeatures.ensure_int("Finishing number:")
                primes_count = Primes.primes_between(num_1, num_2)
                if primes_count == False:
                    print("You typed the same number.")
                elif primes_count == None:
                    print(f"\nThere's no primes between {num_1} and {num_2}.")
                else:
                    print(f"\nThere's {len(primes_count)} primes between {num_1} and {num_2}.")
                    if input("\nDo you want to print them? (Y/n) ") in MainProgram.yes_all_poss:
                        AddFeatures.list_print_format(primes_count)
        
            if choice == "5":
                cont = input("\nThis operation will only stop if you press CTRL + C. Do you want to continue? (Y/n) ")
                if cont in MainProgram.yes_all_poss:
                    num = AddFeatures.ensure_int("Starting number(0):")
                    AddFeatures.kb_inter_handle(Primes.prime_print, num, -1)
            print()
        else:
            return False

    def main():
        AddFeatures.clear()
        while True:
            if MainProgram.menu() == False:
                AddFeatures.clear()
                break
            else:
                print("Press ENTER to go back to MENU. Anything else to EXIT.", end =" ")
                if input() in MainProgram.yes_all_poss:
                    #time.sleep(1)
                    AddFeatures.clear()
                    continue
                else:
                    AddFeatures.clear()
                    break

if __name__ == '__main__':
    MainProgram.main()