msg=input(' Enter nos. : ')
lst=msg.split()
for i in lst:
    if int(i)>0:
        result1 = 'True'
    else:
        result1 = 'False'
        break
for i in lst:
        if i == i[::-1]:
            result2 = 'True'
        else:
            result2 = 'False'

if result1=='True':
    if result2=='True':
        final_result='True'
    else:
        final_result='False'
else:
        final_result='False'
print(final_result)
