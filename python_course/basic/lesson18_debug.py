# Reusing the code from previous lesson in order to learn how to debug.
# if / elif / else
condition1 = False
condition2 = True
condition3 = False
condition4 = True

if condition1:
    print('This is an if code')
else:
    print("First if's else") # The opposite of if.

if 10 == 10:
    print('Another if')

# Another example:
if condition1:
    print("Condition1's code")
elif condition2:
    print("Condition2's code") # This condition is True, than the rest below(if-structure) will be ignored.
elif condition3:
    print("Condition3's code")
elif condition4:
    print("Condition4's code") # Even this one being True.
else:
    print('None condition was satisfied')

print('Out of if')