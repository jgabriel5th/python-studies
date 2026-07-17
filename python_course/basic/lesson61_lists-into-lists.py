'''
List of lists and their indices
'''
rooms = [
    # 0       1
    ['Mary', 'Hellen', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'John', 'Edward', (0, 10, 20, 30, 40)], # 2
]

# print(rooms[0][1]) # [list][value]
# print(rooms[1][0]) # [list][value]
# print(rooms[2][2]) # [list][value]
# print(rooms[2][3][3]) # [list][tuple][tuple-value]

rooms1 = [
    # 0       1
    ['Mary', 'Hellen', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'John', 'Edward', ], # 2
]

for room in rooms1:
    print(f'The room is {room}')
    for student in room:
        print(student)