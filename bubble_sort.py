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
    bubble_sort(my_list)

    # Display the values again, now after ONE PASS of the exchange sort algorithm.
    print("after : ", end="")
    for n in my_list:
        print(f"{n} ", end="")
    print()


def bubble_sort(numbers: List[int]) -> None:
    """Sort a list using the bubble sort algorithm.
    
    Args:
        numbers: the list to sort.
    """
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                swap(numbers, i, i+1)
                swaps += 1


def swap(some_list: List[int], a: int, b: int) -> None:
    """Swaps elements of a list given two index locations.
    
    Args:
        some_list: A list.
        a: First index location
        b: Second index location
    """
    temp = some_list[a]
    some_list[a] = some_list[b]
    some_list[b] = temp


if __name__ == "__main__":
    main()
