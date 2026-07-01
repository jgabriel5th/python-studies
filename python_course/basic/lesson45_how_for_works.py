'''
Iterable -> str, range, etc -> element who has a method __iter__ inside it.
Iterator -> the one who delivers one value at a time.
next -> deliver me the next value.
iter -> deliver me your iterator.
'''
# text = iter('John') # __iter__()
# print(next(text)) # __next__()
# print(next(text))
# print(next(text))
# print(next(text))
# print(next(text)) # It'll raise an exception called StopIteration

# How for works:
# for letter in text:
text = 'John' # iterable
iterator = iter(text) # iterator

while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break