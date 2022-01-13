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
    exchange_sort(my_list)

    # Display the values again, now after ONE PASS of the exchange sort algorithm.
    print("after : ", end="")
    for n in my_list:
        print(f"{n} ", end="")
    print()


def exchange_sort(numbers: List[int]) -> None:
    """Sort a list using the exchange sort algorithm.
    
    Args:
        numbers: the list to sort.
    """
    marker = 0
    while marker < len(numbers) - 1:
        for i in range(marker+1, len(numbers)):
            if numbers[marker] > numbers[i]:
                swap(numbers, marker, i)
        marker += 1


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
