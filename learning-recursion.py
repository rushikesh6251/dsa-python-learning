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
def swaparr1(l,r):
    if l>=r:
        print(a)
        return
    a[l],a[r]=a[r],a[l]
    swaparr1(l+1,r-1)
def swaparr2(l):
    global i
    if l>=n-i-1:
        print(a)
        return
    a[l],a[n-i-1]=a[n-i-1],a[l]
    i+=1
    swaparr2(l+1)

def pallin_string(i):
    global a,n
    if i/2>=len(a):
        return True
    elif a[n - i - 1] != a[i]:
        return False
    return(i+1)
if __name__=="__main__":
    a="MADSM"
    n=len(a)# count = 0
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
def swaparr1(l,r):
    if l>=r:
        print(a)
        return
    a[l],a[r]=a[r],a[l]
    swaparr1(l+1,r-1)
def swaparr2(l):
    global i
    if l>=n-i-1:
        print(a)
        return
    a[l],a[n-i-1]=a[n-i-1],a[l]
    i+=1
    swaparr2(l+1)

def pallin_string(i,a):
    if i>=len(a)//2:
        return True
    if a[i]!=a[len(a) - i - 1] :
        return False
    return pallin_string(i+1,a)
if __name__=="__main__":
    a="MADAM"
    print(pallin_string(0,a))