final_lst=[]
total_lst=[]
nested_lst=[]
temp_grade=[]
n=int(input(' No. of Students : '))
for i in range(n):
    name=input(' Enter Student Name : ')
    grade=float(input(' Enter Grade : '))
    nested_lst.append(name)
    nested_lst.append(grade)
    total_lst.append(nested_lst)
    temp_grade.append(grade)
    nested_lst=[]
temp_grade.remove(min(temp_grade))
found=min(temp_grade)
for i in range(n):
    if total_lst[i][1]==found:
        final_lst.append(total_lst[i][0])
final_lst = sorted(final_lst)
for i in final_lst:
    print(i)
