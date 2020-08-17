from timeit import timeit
from math import floor


def linearSearch(arr, item):
    for i in arr:
        if (i == item):
            return True
    return False


def binarySearch(arr, targetValue):
    # array = sorted(arr) to prevent overtime
    array = arr
    min = 0
    max = len(array) - 1

    while True:
        average = floor((min + max) / 2)
        if (max < min):
            return False
        if (array[average] == targetValue):
            return True
        if (array[average] < targetValue):
            min = average + 1
        else:
            max = average - 1


first7Primes = [2, 3, 5, 7, 11, 13, 17]

# First calculation set
print('Small set of numbers')
print(f'Linear takes {timeit(lambda: linearSearch(first7Primes, 5))} seconds')
print(f'Binary takes {timeit(lambda: binarySearch(first7Primes, 5))} seconds')

def largeNumberSet(max):
    numbers = []
    for i in range(max):
        numbers.append(i)
    return numbers


firstOneThousandNumbers = largeNumberSet(1000)

# Second calculation set
print('Large set of numbers')
print(f'Linear takes {timeit(lambda: linearSearch(firstOneThousandNumbers, 422))} seconds')
print(f'Binary takes {timeit(lambda: binarySearch(firstOneThousandNumbers, 422))} seconds')
