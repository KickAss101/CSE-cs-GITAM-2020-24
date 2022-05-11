#! /usr/bin/python3

def reverse_fact(n):
    if n == 1:
        return 1
    if n <= 0:
        return -1

    i = 2

    while n > 1:
        if n % i != 0:
            return -1

        n /= i
        i += 1

    return i - 1

if __name__ == "__main__":
    n = int(input("Enter factorial: "))

    fact = reverse_fact(n)

    print(f"Reverse factorial of {n} is {fact}")
