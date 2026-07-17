'''
split and join with list and str
split - split a str
join - join a str
'''
sentence = '    That is such   , an interesting phrase      '
words_list = sentence.split() # It'll split by the whitespaces, if nothing is put into ().
phrases_list_raw = sentence.split(',') # Now it'll split by the ,

phrases_list = []
for i, phrase in enumerate(phrases_list_raw):
    phrases_list.append(phrases_list_raw[i].strip())

print(words_list)
print(phrases_list_raw)
print(phrases_list)
join_phrase = ', '.join(phrases_list)
print(join_phrase)