'''
Make a shopping list with lists.
The user must be able to insert, delete and list the values
from your list.
Don't permit the program to break with errors from non-existent
indices in the list.
'''
shopping_list = ('Bread', 'Pancake', 'Apple', 'Milk', 'Juice')
value_list = (1.50, 2.00, 3.00, 1.00, 2.50)
shopping_list1 = []

while True:
    print(f'These are our available items: {shopping_list}')
    choice = input('Press [I] to insert an item, [D] to delete, [L] to list the values or [Q] to quit: ').lower()
    list_value = choice == 'l'
    insert = choice == 'i'
    delete = choice == 'd' and shopping_list1
    quit_program = choice == 'q'

    if insert:
        item = input('Which item do you want to insert? ').capitalize()
        if item in shopping_list:
            shopping_list1.append(item)
            print(f'{item} was added to the list!')
        else:
            print('This item is not available.')

    elif delete:
        print(f'Items in your shopping list: {shopping_list1}')
        remove = input('Choose the item you wish to remove: ').capitalize()
        if remove in shopping_list:
            shopping_list1.remove(remove)
        else:
            print("This item doesn't exist in your shopping list or was typed wrongly")

    elif list_value:
        for product, price in zip(shopping_list, value_list):
            print(f'{product} costs ${price:.2f}')
    
    elif quit_program:
        print(f'These were the products you bought: {shopping_list1}')
        print('Thanks for using the shopping list!')
        break
        
                
