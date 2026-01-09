def selection(a):
    for i in range(len(a)-1):
        min1=i
        for j in range(i+1,len(a)):
            if a[j]<=a[min1]:
                min1=j
        a[min1],a[i]=a[i],a[min1]
    print(a)
def bubble(a):
    swap1=0
    for i in range(n-1,1,-1):
        for j in range(0,i,+1):
            if a[j]>=a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]
                swap1=1
        if swap1==0:
            print("already sorted array...exiting")
            break
    print(a)

def insertion(a):
    for i in range(len(a)):
        j=i
        while j>0 and a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1
    print(a)
if __name__=="__main__":
    n=int(input("enter size of array: "))
    a=[]
    for i in range(n):
        a.append(int(input("enter array element: ")))
    insertion(a)