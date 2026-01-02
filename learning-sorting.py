def selection(a,n):
    for i in range(n-2):
        min1=i
        for j in range(i,n-1):
            if a[j]<=min1:
                min1=j
        a[min1],a[i]=a[i],a[min1]
    print(a)

if __name__=="__main__":
    n=int(input("enter size of array: "))
    a=[]
    for i in range(n):
        a.append(int(input("enter array element: ")))
    # print(a)
    selection(a,n)