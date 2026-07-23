'''
args - Non-named arguments(positional)
* - *args (packing and unpacking)
'''
# Reminder of unpacking
x, y, *_ = 1, 2, 3, 4
print(x, y, _)

# def sumNumbers(x, y):
#     return x + y

def sumNumbers(*args): # It allows to receive unlimited arguments just like print()
    # it creates a tuple in args.
    total = 0
    for number in args:
        print(f'Sum: {total} + {number}')
        total += number
        print('Total:', total)


sumNumbers(1, 2, 3, 4, 5)