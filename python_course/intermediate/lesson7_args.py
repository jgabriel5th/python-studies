'''
args - Non-named arguments(positional)
* - *args (packing and unpacking)
'''
# Reminder of unpacking
x, y, *_ = 1, 2, 3, 4
print(x, y, _)

# def sumNumbers(x, y):
#     return x + y

# def sumNumbers(*args): # It allows to receive unlimited arguments just like print()
#     # it creates a tuple in args.
#     total = 0
#     for number in args:
#         print(f'Sum: {total} + {number}')
#         total += number
#         print('Total:', total)
#     return total

def sumNumbers(*args): # It allows to receive unlimited arguments just like print()
    # it creates a tuple in args.
    total = 0
    for number in args:
        total += number
    return total


sum_numbers = sumNumbers(1, 2, 3, 4, 5, 6, 7, 8)
numbers = 1, 2, 3, 4, 5, 6, 7, 8
print(sumNumbers(*numbers)) # *unpacking in order to avoid creating a tuple inside a tuple in args.
print(sum(numbers)) # Python has a function that sums numbers.