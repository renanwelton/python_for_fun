divs = []

def ensure_int(ask):
    """ Works like input(), but ensures the input is an integer > 0. """
    while True:
        print("\n" + ask, end = " ")
        try:
            num = int(input())
            if num < 1:
                print("\nPositive integers only.")
                continue
            return num
        except ValueError:
            print("\nThat's not even close to an integer.")

def prop_divs(num):
    """ Finds all whole divisors of a number, including 1. """
    for n in range(1, num//2+1):
        if num % n == 0:
            divs.append(n)
    return divs

def perf_num(num):
    return sum(prop_divs(num)) == num

def main():
    print("\nLet's find perfect numbers.")
    num = ensure_int("Type a positive number:")
    
    if perf_num(num):
        print("\nYes,", num, "is a perfect number.\nIt's divisors are:", end = " ")
        for n in divs:
            if not n == divs[-1]:
                print(n, end = ", ")
            else:
                print(str(divs[-1]) + ".")
        print()
    else:
        print("\nNo,", num, "is not a perfect number.\n")

    question = input("Wanna try again? (Y/n) ")
    if question in ["Yes", "yes", "Y", "y", ""]:
        main()
    print()

if __name__ == "__main__":
    main()

    ## Debug code ##

    """num = 1
    while True:
        result, divisors = perf_num(num)
        if result:
            print(num)
        num += 1"""