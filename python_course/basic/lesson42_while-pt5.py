sentence = 'Python is a programming language'\
'multi-paradigm. '\
'Python was created by Guido van Rossum.'
# print(sentence.count('Python')) # count() is a str method used to count how many times a chosen caractere appeared.

i = 0
qty_appeared_more_often = 0
letter_appeared_more_often = ''

while i < len(sentence):
    actual_letter = sentence[i]

    if actual_letter == ' ':
        i += 1
        continue

    current_qty = sentence.count(actual_letter) # it'll count each iteration.

    if qty_appeared_more_often < current_qty:
        qty_appeared_more_often = current_qty
        letter_appeared_more_often = actual_letter

    i += 1

print(
    'The letter that appeared more often was '
     f'"{letter_appeared_more_often}" that appeared '
     f'{qty_appeared_more_often}x'
     )