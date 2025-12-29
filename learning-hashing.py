if __name__=="__main__":
# Input
    n = int(input("enter size of array: "))
    arr = []
    for _ in range(n):
        value = int(input("enter array element and press ENTER: "))
        arr.append(value)

    # precompute
    hash1=[0]*13   #13 is the size of hash array consisting zeros
    for i in range(n):
        hash1[arr[i]]+=1
    print(hash1)

    # fetching
    q=int(input("enter how many numbers you want to count appearance of: "))
    for i in range(q):
        number=int(input("enter number to find its occurance: "))
        if number>q:
            print("enter element within array size")
            break
        # fetch
        print(hash1[number])


