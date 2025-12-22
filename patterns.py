
def pattern7(n):
    for i in range(n):
        # spaces
        for j in range(n-i-1):
            print(" ",end="")
        # stars
        for k in range(2*i+1):
            print("*",end="")
        # spaces
        for l in range(n-i-1):
            print(" ",end="")
        print("\n")
def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(2*n-(2*i+1)):
            print("*",end="")
        for l in range(i):
            print(" ",end="")
        print("\n")
def pattern9(n):
    for i in range(n):
        # spaces
        for j in range(n-i-1):
            print(" ",end="")
        # stars
        for k in range(2*i+1):
            print("*",end="")
        # spaces
        for l in range(n-i-1):
            print(" ",end="")
        print("\n")
    for a in range(n):
        # spaces
        for b in range(a):
            print(" ",end="")
        # star
        for c in range(2*n-(2*a+1)):
            print("*",end="")
        # spaces
        for d in range(a):
            print(" ",end="")
        print("\n")
def pattern10(n):
    for i in range(n):
        for k in range(i):
            print("*",end="")
        print("\n")
    for a in range(n):
        for b in range(n-a):
            print("*",end="")
        print("\n")
def pattern11(n):
    start=1
    for i in range(n):
        if i%2==0:
            start=1
        else:
            start=0
        for j in range(i):
            print(start,end=" ")
            start=1-start
        print("\n")
def pattern12(n):
    space=2*(n-1)
    # numbers
    for i in range(1,n):
        for j in range(1,i+1):
            print(j,end="")

        # #spaces
        for j in range(2,space):
            print(" ",end="")

        #numbers
        for j in range(i,0,-1):
            print(j,end="")
        print("\n")
        space -= 2
def pattern13(n):
    value = 1
    for i in range(n):
        for j in range(i):
            print(value,end=' ')
            value+=1
        print("\n")
def pattern14(n):
    char="A"
    for i in range(n):
        for j in range(i):
            print(char,end="")
            char=chr(ord(char) + 1)
        char="A"
        print("\n")
    # completed
def pattern15(n):
    for i in range(n):
        for j in range(n - i):
            print(chr(ord('A') + j), end="")
        print()
    # here we use chr and ord functions to print the further sequence of the alphabet "A"
def pattern16(n):
    char="A"
    for i in range(n):
        for j in range(-1,i):
            print(char,end="")
        char=chr(ord(char) + 1)
        print("\n")
    # completed
def pattern17(n):
    for i in range(n):
        # spaces
        for j in range(n-i-1):
            print(" ",end="")
        # alphabets
        char="A"
        breakpoint1=(2*i+1)/2-1
        for k in range(2*i+1):
            print(char,end="")
            if k <=  breakpoint1:
                char = chr(ord(char) + 1)
            else:
                char = chr(ord(char) - 1)

        # spaces
        for l in range(n-i-1):
            print(" ",end="")
        print("\n")
def pattern18(n):
    final_char=chr(ord("A")+n-1)
    for i in range(n):
        for j in range(ord(final_char)-i,ord(final_char)+1):
            print(chr(j), end="")
        print("\n")
def pattern19(n):
    inis=0
    for i in range(n):
        # stars
        for j in range(n-i):
            print("*",end="")
        # spaces
        for k in range(inis):
            print(" ",end="")
        # stars
        for l in range(n-i):
            print("*",end="")
        print("\n")
        inis+=2
    inis=8
    for i in range(n):
        # stars
        for b in range(i+1):
            print("*",end="")
        # spaces
        for c in range(inis):
            print(" ",end="")
        # stars
        for d in range(i+1):
            print("*",end="")
        print("\n")
        inis-=2

if __name__ == "__main__":
    n=5
    pattern19(n)

