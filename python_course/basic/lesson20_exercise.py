# An exercise from the Python Course
first_value = input('Type a value: ') # Though it's a String, it works without converting to int or float.
second_value = input('Type another value: ') # It's related to UNICODE table.

if first_value >= second_value:
    print(f'{first_value=} is greater or equal to {second_value=}')
elif second_value > first_value:
    print(f'{second_value=} is greater or equal to {first_value=}')
else:
    print("You didn't type correctly")