
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
if __name__ == "__main__":
    n=111
    palindrome(n)