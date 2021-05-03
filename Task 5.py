lower=''
upper=''
odd=''
even=''
msg=input(' Enter a string ')
a=sorted(msg)
for i in a:
        if i.isupper():
            upper+=i
        elif i.islower():
            lower+=i
        elif int(i)%2==0:
            even+=i
        elif int(i)%2==1:
            odd+=i
print(lower+upper+odd+even)
        
