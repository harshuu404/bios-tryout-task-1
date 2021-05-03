msg=input(' Enter nos. to multiply : ')
multiply = 1
lst = msg.split()
for i in lst:
    multiply = multiply * int(i)
print(multiply)
