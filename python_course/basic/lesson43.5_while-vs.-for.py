# while is commonly used when the number of iteraction is unknown
# for is used when the number of iteraction is known

# Iteracting a string with while(hard):
word = input('Type something: ')
i = 0

while i < len(word):
    word_index = word[i]
    print(word_index)
    i += 1

# Iteracting a string with for(easy):
word1 = input('Type something: ')
for index in word1:
    print(index)