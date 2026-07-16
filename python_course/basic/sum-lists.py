list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 5, 6, 2, 5, 2]
sum1 = 0
for number1 in list1:
    sum1 += number1
    print(f'{sum1}')

total = sum(list2) # sum() function
print(total)