from functools import reduce

my_number = [20,30,40,50]


def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_number, 0))
    