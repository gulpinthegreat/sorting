import random
from typing import List


def main():
    # generate random my_listay
    my_list = [random.randrange(100) for _ in range(10)]

    # Display the original (unsorted values)
    print("before: ", end="")
    for n in my_list:
        print(f"{n} ", end="")
    print()

    # sort
    selection_sort(my_list)

    # Display the values again, now after ONE PASS of the exchange sort algorithm.
    print("after : ", end="")
    for n in my_list:
        print(f"{n} ", end="")
    print()
