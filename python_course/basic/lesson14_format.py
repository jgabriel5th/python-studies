a = 'A'
b = 164.9
c = 2540
string = 'b={name2}, a={name1}, b={name2:.2f}, c={name3:,.2f}'
formato = string.format(
    name1=a, # <- Named parameter(name1, name2, name3)
    name2=b, # Arguments = a, b, c
    name3=c    
)

print(formato)