import os
'''
Make a game for the user to guess what is the secret word.
- You're going to propose any secret word and give the possibility for the
user to type only a letter.
- After the user type the letter, you're going to check if the typed letter is in
the secret word.
    - If the typed letter is in the secret word; print the letter;
    - If the typed letter is not in the secret word; print *.
Make the attempt count of your user.
'''


secret_word = 'judo'
right_letter = ''
attempts = 0
print('Tip: the secret word is a martial art born in Japan.')
while True:
    typed_letter = input('Guess the secret word by typing a letter at a time: ').lower()
    attempts += 1

    if len(typed_letter) > 1:
        print('Only one letter is permitted')
        continue

    if typed_letter in secret_word:
        right_letter += typed_letter # Concatenation
    
    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in right_letter:
            formed_word += secret_letter
        else:
            formed_word += '*'
    
    print('Formed word:', formed_word)

    if formed_word == secret_word:
        os.system('clear')
        print('You won! Congratulations!')
        print('Total attempts: ', attempts)
        break