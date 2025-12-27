# count = 0
# sum=0
def f():
    # this shows infinite recursion
    print("1")
    f()
def f1():
    global count
    if count ==4 :
        return
    print(count)
    count+=1
    f1()
def pname(i,n):
    global count
    if i > n:
        return
    print("Rushikesh")
    pname(i+1,n)
def pnum(i,n):
    if i>n:
        return
    print(i)
    pnum(i+1,n)
def prnum(i,n):
    if i<1:
        return
    print(i)
    prnum(i-1,n)
def psum(i,n):
    global sum
    if i > n:
        print("the sum of",n,"numbers is: ", sum)
        return
    sum = sum + i
    psum(i + 1, n)
def btpnum(i,n):
    if i <1:
        return
    btpnum(i-1,n)
    print(i)
def btprnum(i,n):
    if i >n:
        return
    btprnum(i+1,n)
    print(i)
def sumaw(n):
    if n==0:
        return 0
    return n+ sumaw(n-1)
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
if __name__=="__main__":
    n=int(input("enter any integer: "))
    print(sumaw(n))