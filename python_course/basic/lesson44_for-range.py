'''
For + Range
range -> range(start, stop, step)
'''
numbers = range(0, 11, 2) # The stop-digit is usually ignored in Python, so is 0 until 10 in this case.
# It's possible to put negative numbers as well: range(0, -10, -1) <- example

for number in numbers:
    print(number)

