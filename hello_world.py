# students=[]
# n=1
# for i in range(n): 
#     name=input("enter student name:")
#     marks=float(input("enter his/her marks: "))
#     students.append([name,marks])
#     print(students)

s = input()
a=b=c=d=e=False
for i in s:
    if i.isalnum():
        a=True
    if i.isalpha():
        b=True
    if i.isdigit():
        c=True
    if i.islower():
        d=True
    if i.isupper():
        e=True
if a:
    print(a)
if b:
    print(b)
if c:
    print(c)
if d:
    print(d)
if e:
    print(e)    