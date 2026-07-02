# continue, break and else also can be used with for-structure.
for i in range(10):
    if i == 2:
        print('i is 2, jumping...')
        continue

    if i == 8:
        print('i is 8, your else will not execute')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('For completed with success!')

