"""
Creating Collatz sequences
"""
import sys


def collatz(number):
    """
    Returns the next value in a collatz sequence
    :param number:
    :return: number:
    """
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    print("Enter a number:")
    try:
        x = int(input())
        break
    except ValueError:
        print("Please enter a valid integer value")
        # sys.exit()

while x != 1:
    x = collatz(x)

