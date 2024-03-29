# TO-DO:
# Remove loop from ensure_int
# If GUI is too much, try a simple menu rework
# Pass only odd numbers to primes_between
# Show temps in real-time upon callig any Benchmark() method
# Pseudo GUI in the likes of cfdisk (Maybe someday)

import math
import time
import os
import multiprocessing

OPERATIONS = (range(1,7))
YES = ("Yes", "yes", "Y", "y", "")


class Primes:
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

    def dumb_prime_check(self, num):
        """Checks every division up to 'num' and uses a while loop.
        Should be slow enough.

        It's even dumbier when I look back and remember this
        was one my first iterations."""
        div = 2
        while True:
            if num % div == 0 and num != 2 or num < 2:
                return False
            else:
                div += 1
                if div >= num or num == 2:
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
            if self.prime_check(num):
                print(num) 
                loop = loop - 1
            num += 2

    def prime_between(self, num_1, num_2):
        """Finds out how many primes exist between 2 given numbers. 
        Excludes the numbers themselves.

        Returns a list if any prime is found.
        
        Returns 'False' if the given numbers are the same.
        
        Returns 'None' if the are no primes between the given numbers."""
        primes_list = []
        if num_1 < num_2:
            # Everythig from this point down to the for loop should be replaced with a function.
            if num_1 < 2:
                primes_list.append(2)
                num_1 = 2
            if not num_1 % 2 == 0:
                num_1 += 1 # Adds 1 to odd numbers.
            num_1 += 1 # Makes range start from next number.
            for i in range(num_1, num_2, 2):
                if self.prime_check(i):
                    primes_list.append(i)
        elif num_1 > num_2:
            if num_2 < 2:
                primes_list.append(2)
                num_2 = 2
            if not num_2 % 2 == 0:
                num_2 += 1
            num_2 += 1
            for i in range(num_2, num_1, 2):
                if self.prime_check(i):
                    primes_list.append(i)
        else:
            return False
                    
        if len(primes_list) == 0:
            return None
        else:
            return primes_list

    def list_prime_check(self, num):
        """Instead of returning a boolean, returns 
        the actual number so you can create a list."""
        if num == 2:
            return num
        if num < 2 or num % 2 == 0:
            return
        sqrt = int(math.sqrt(num))
        for div in range(3, sqrt+1, 2):
            if num % div == 0:
                return 
        return num
    
    def fast_prime_between(self, num_1, num_2):
        """Multitheaded version of primes between.
        May crash due to limited RAM when computing a big range."""
        temp_list = []
        primes_list = []
        pool = multiprocessing.Pool(processes=bench.cpu_count)
        if num_1 < num_2:
            num_range = range(num_1+1, num_2)
        elif num_1 > num_2:
            num_range = range(num_1-1, num_2, -1)  
        else:
            return False
        
        temp_list = pool.map(self.list_prime_check, num_range)
        for item in temp_list:
            if not temp_list[item] == None:
                primes_list.append(temp_list[item])

        if len(primes_list) == 0:
            return None
        else:
            return primes_list

    def prime_next(self, num):
        """Returns the next prime of a given number."""
        num += 1
        while not self.prime_check(num):
            num += 1
        return num

    def prime_prev(self, num):
        """Returns the previous prime of a given number bigger than 2.
        Returns False otherwise."""
        if num <= 2:
            return False
        num -= 1
        while not self.prime_check(num):
            num -= 1
        return num


class Benchmark:
    # Uses AMD's R5-5600 singlethreaded performance as baseline for a score close to 1000 points.
    points = 25000 # 25.000 default. 
    # Tied-up to points (25.000). Changing this also changes final score.
    numbers = range(10_000_000) # 10.000.000 default. Uses about 100MB of RAM.
    cpu_count = os.cpu_count()
    
    def singlecore_benchmark(self):
        """Single-Thread performance test using Python."""
        pool = multiprocessing.Pool(processes=1)
        start = time.time()
        pool.map(prime.prime_check, self.numbers)
        end = time.time()
        print(f"Test took {round(end - start, 2)} seconds.\n")
        return int(self.points / (end - start))

    def multicore_benchmark(self):
        """Multi-Thread performance test using Python."""
        pool = multiprocessing.Pool(processes=self.cpu_count) 
        start = time.time()
        pool.map(prime.prime_check, self.numbers)
        end = time.time()
        print(f"Test took {round(end - start, 2)} seconds.\n")
        return int(self.points / (end - start))
    
    def cpu_synthetic_load(self):
        """Synthetic CPU load using prime calculation.""" 
        pool = multiprocessing.Pool(processes=self.cpu_count)
        while True:
            # Using dumb_prime_check here makes the thread usage graph look flat. 
            # Thanks to Lucas for the idea.
            pool.map(prime.dumb_prime_check, self.numbers)

def ensure_int(string):
    """Works like input(), but ensures the input is an integer.
    Returns 0 by default."""
    while True:
        print(f"\n{string}", end=" ")
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

        if choice == 1:
            num = ensure_int("What number do you want to check?")
            if prime.prime_check(num):
                print(f"\nYes, {num} is prime.")
            else:
                print(f"\nNo, {num} is not prime.")
                
        elif choice == 2:
            num = ensure_int("Starting number(0):")
            loop = ensure_int("How many primes do you want to print?")
            print()
            prime.prime_print(num, loop)

        elif choice == 3:
            num = ensure_int("Previous and next primes of what number?")
            prev = prime.prime_prev(num)
            next = prime.prime_next(num)
            if prev is False:
                print(f"\n{num} has no previous primes. The next is {next}.")
            else:
                print(f"\nThe previous prime of {num} is {prev}. The next is {next}.")
    
        elif choice == 4:
            num_1 = ensure_int("Starting number(0):")
            num_2 = ensure_int("Finishing number:")
            print("\n1 - Fast calculation (may crash with high numbers due to high RAM usage)\n2 - Slow (but safe)")
            choice = ensure_int("What's your choice?")
            if choice in range(1,3):
                print("\nDon't worry in case you are stuck here, some calculations are being done.")
                if choice == 1:
                    primes_list = prime.fast_prime_between(num_1, num_2)
                if choice == 2:
                    primes_list = prime.prime_between(num_1, num_2)

                if primes_list == False:
                    print("\nYou typed the same number.")
                elif primes_list == None:
                    print(f"\nThere's no primes between {num_1} and {num_2}.")
                else:
                    print(f"\nThere's {len(primes_list)} primes between {num_1} and {num_2}.")
                    if input("\nDo you want to print them? (Y/n) ") in YES:
                        list_print_format(primes_list)
        
        elif choice == 5:
            cont = input("\nThis operation will only stop if you press CTRL + C. Do you want to continue? (Y/n) ")
            if cont in YES:
                num = ensure_int("Starting number(0):")
                kb_inter_handler(prime.prime_print, num, -1)

        elif choice == 6:
            print("\n1 - Singlethead\n2 - Multithread\n3 - Stress Test (may crash due to high RAM usage)")
            choice = ensure_int("What's your choice?")
            if choice in range(1,4):
                print("\nDoing some math...\n")
                if choice == 1:
                    print(bench.singlecore_benchmark())
                if choice == 2:
                    print(bench.multicore_benchmark())
                if choice == 3:
                    print("Press Ctrl + C to stop it.")
                    bench.cpu_synthetic_load()
    else:
        return False

def main():
    clear()
    while True:
        if menu() == False:
            clear()
            break
        else:
            print()
            print("Press ENTER to go back to MENU. Anything else to EXIT.", end =" ")
            answer = input()
            if answer in YES:
                time.sleep(1)
                clear()
                continue
            else:
                clear()
                break

prime = Primes()
bench = Benchmark()

if __name__ == '__main__':
    main()