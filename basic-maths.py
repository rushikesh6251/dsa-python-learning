
def printdigits(n):
    # this lets you print the digits in the given number
    while n>0:
        lastdigit=n%10
        print(lastdigit)
        n=n//10
def countdigits(n):
    # this lets you count the number of digits in the given number
    count=0
    while n>0:
        # lastdigit=n%10
        count+=1
        n=n//10
    print(count)
def reverse(n):
    reversed1=0
    while n>0:
        lastdigit=n%10
        n=n//10
        reversed1=(reversed1*10)+lastdigit
    print(reversed1)
def palindrome(n):
    reversed1 = 0
    n1=n
    while n > 0:
        lastdigit = n % 10
        n = n // 10
        reversed1 = (reversed1 * 10) + lastdigit
    if reversed1 == n1:
        print("the number given is palindrome")
    else:
        print("the given number is not palindrome")
def armstrong(n):
    n1=n
    value=0
    while n>0:
        lg=n%10
        value = lg*lg*lg + value
        n=n//10
    if value == n1:
        print(True)
    else:
        print(False)
def printdivisors(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i)
        i+=1
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count == 2:
            print("it is a prime number")
    else:
        print("it is not a prime number")
def gcd(n,m):
    gcd=0
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            gcd=i
    print("GCD is ",gcd)

if __name__ == "__main__":
    n=20
    m=400
    gcd(n,m)