import math
import time
import os
import multiprocessing as mp

OPERATIONS = (range(1,7))
YES = ("Yes", "yes", "Y", "y", "")


class Benchmark:
    points = 25000
    cpu_count = os.cpu_count()
    numbers = range(10_000_000)
    
    def singlecore_benchmark(self):
        """Single-Thread performance test using Python.

        Uses AMD's R5-5600 singlethreaded performance as baseline for a score close to 1000 points.
        That's why I use 25k in points.

        Should not be used for anything other than dick measuring among friends."""
        pool = mp.Pool(processes=1)
        start = time.time()
        pool.map(po.prime_check, self.numbers)
        end = time.time()
        return int(self.points / (end - start))

    def multicore_benchmark(self):
        """Multi-Thread performance test using Python.

        Should not be used for anything other than dick measuring among friends."""
        pool = mp.Pool(processes=self.cpu_count) 
        start = time.time()
        pool.map(po.prime_check, self.numbers)
        end = time.time()
        return int(self.points / (end - start))


class PrimeOperations:
    def prime_check(self, num):
        """Checks if a given integer is prime."""
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        sqrt = int(math.sqrt(num))
        for div in range(3, sqrt+1, 2):
            if num % div == 0:
                return False
        return True

    def prime_print(self, num, loop):
        """Only prints prime numbers up to n times.
        Passing a negative value to loop causes it to loop indefinitely."""          
        if num < 2 or num % 2 == 0:
            if num < 2:
                num = 2
                print(num)
                num += 1
            else:
                num += 1
        while not loop == 0:
            if po.prime_check(num):
                print(num) 
                loop = loop - 1
            num += 2

    def prime_between(self, num_1, num_2):
        """Finds out how many primes exist between 2 given numbers. 
        Excludes the numbers themselves.

        Returns a list if any prime is found.
        
        Returns 'False' if the given numbers are the same or if I borked the code.
        
        Returns 'None' if the are no primes between the given numbers.
        """
        print("\nDon't worry in case you are stuck here, some calculations are being done.")
        primes_count = []
        if num_1 < num_2:
            for i in range(num_1 + 1, num_2):
                if po.prime_check(i):
                    primes_count.append(i)
        elif num_1 >num_2:
            for i in range(num_2 + 1, num_1):
                if po.prime_check(i):
                    primes_count.append(i)
        else:
            return False
                    
        if len(primes_count) == 0:
            return None
        else:
            return primes_count

    def prime_next(self, num):
        """Returns the next prime of a given number."""
        while not po.prime_check(num + 1):
            num += 1
        return num + 1

    def prime_prev(self, num):
        """Returns the previous prime of a given number bigger than 2.
        Returns False otherwise."""
        if num <= 2:
            return False
        while not po.prime_check(num - 1):
            num -= 1
        return num - 1
      
def ensure_int(ask):
    """Works like input(), but ensures the input is an integer.
    Returns 0 by default."""
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

def kb_inter_handler(func, *args):
    """Handles Keyboard Interruption.
    Receives a function and it's arguments separately."""
    try:
        func(*args)
    except KeyboardInterrupt:
        time.sleep(1)
        print("\nYou did the right thing, don't worry.")

def list_print_format(list):
    """Prints every element in a list separating them by a comma.
    The last element is printed with a dot."""
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

def menu():
    print("\n --- WELCOME TO PRIMEBENCH ---\n")
    print("1 - Check if given number is prime.")
    print("2 - Print set amount of primes.")
    print("3 - Print next and previous primes of a number.")
    print("4 - Find primes between two numbers")
    print("5 - Generate primes indefinitely.")
    print("6 - Benchmarks.\n")
    print("To exit press anything else.")

    choice = (ensure_int("Choose operation:"))

    if choice in OPERATIONS:

        if choice is 1:
            num = ensure_int("What number do you want to check?")
            if po.prime_check(num) == True:
                print(f"\nYes, {num} is prime.")
            else:
                print(f"\nNo, {num} is not prime.")
                
        if choice is 2:
            num = ensure_int("Starting number(0):")
            loop = ensure_int("How many primes do you want to print?")
            print()
            po.prime_print(num, loop)

        if choice is 3:
            num = ensure_int("Previous and next primes of what number?")
            if po.prime_prev(num) == False:
                print(f"\n{num} has no previous primes. The next is {po.prime_next(num)}.")
            else:
                print(f"\nThe previous prime of {num} is {po.prime_prev(num)}. The next is {po.prime_next(num)}.")
    
        if choice is 4:
            num_1 = ensure_int("Starting number(0):")
            num_2 = ensure_int("Finishing number:")
            primes_count = po.prime_between(num_1, num_2)
            if primes_count == False:
                print("You typed the same number.")
            elif primes_count == None:
                print(f"\nThere's no primes between {num_1} and {num_2}.")
            else:
                print(f"\nThere's {len(primes_count)} primes between {num_1} and {num_2}.")
                if input("\nDo you want to print them? (Y/n) ") in YES:
                    list_print_format(primes_count)
    
        if choice is 5:
            cont = input("\nThis operation will only stop if you press CTRL + C. Do you want to continue? (Y/n) ")
            if cont in YES:
                num = ensure_int("Starting number(0):")
                kb_inter_handler(po.prime_print, num, -1)

        if choice is 6:
            print("\n1 - Singlecore\n2 - Multicore")
            choice = ensure_int("What's your choice?")
            if choice in [1, 2]:
                print("\nDoing some math...\n")
                if choice == 1:
                    print(bm.singlecore_benchmark())
                if choice == 2:
                    print(bm.multicore_benchmark())
        print()
    else:
        return False

def main():
    clear()
    while True:
        if menu() == False:
            clear()
            break
        else:
            print("Press ENTER to go back to MENU. Anything else to EXIT.", end =" ")
            if input() in YES:
                time.sleep(1)
                clear()
                continue
            else:
                clear()
                break

po = PrimeOperations()
bm = Benchmark()

if __name__ == '__main__':
    main()