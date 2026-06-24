name = 'John'
height = 1.80
weight = 90
bmi = weight / height ** 2
number = 1050.250


#f-string
line = f'{name} is {height:.2f}m tall, weighs {weight}kg and their BMI is {bmi}'
fnumber = f'{number:,.2f}' # ,. is useful for money representation.
print(fnumber)
print(line)