def ensure_int(ask):
    """ Works like input(), but ensures the input is an integer > 0. """
    while True:
        print(f"\n{ask}", end=" ")
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
    divs = []
    for n in range(1, num//2+1):
        if num % n == 0:
            divs.append(n)
    return divs

def perf_num(num, divs):
    return sum(divs) == num

def main():
    print("\nLet's find perfect numbers.")
    num = ensure_int("Type a positive number:")
    divs = prop_divs(num)
    if perf_num(num, divs):
        print(f"\nYES, {num} is a perfect number.\nIt's divisors are:", end=" ")
        for n in divs:
            if not n == divs[-1]:
                print(n, end=", ")
            else:
                print(f"{divs[-1]}.")
        print()
    else:
        print(f"\nNO, {num} is not a perfect number.\n")

    question = input("Wanna try again? (Y/n) ")
    if question in ["Yes", "yes", "Y", "y", ""]:
        main()
    print()

if __name__ == "__main__":
    main()