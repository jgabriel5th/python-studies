# while is commonly used when you don't know how many iteractions will happen.
# saved_password = '123456'
# typed_password = ''
# repetitions = 0

# while saved_password != typed_password:
#     typed_password = input(f'Your password ({repetitions}x): ')

#     repetitions += 1

# print(f'You took {repetitions}x to get your password right.')

text = 'Python'
new_text = ''

for letter in text: # letter is a variable that'll receive the iteraction from variable text.
    new_text += f'*{letter}'
    print(letter)
print(new_text + '*')
