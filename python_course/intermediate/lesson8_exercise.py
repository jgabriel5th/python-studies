# Exercises with functions

# Create a function that multiply all the non-named arguments received.
# Return the total to a variable and print the variable value.

# Create a function that discovers if a numbers is even or odd.
# Return if the number is even or odd.

def multiNumbers(*args):
    total = 1
    for number in args:
        total *= number
    return total

multiply1 = multiNumbers(10, 20, 30, 40, 50)
print(multiply1)


def isEven(number):
    even = number % 2 == 0
    if even:
        return f'{number} is an even number'
    return f'{number} is an odd number' # else is redundant in this case.

print(isEven(19))