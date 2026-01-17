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

def ms(a,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    ms(a,low,mid)
    ms(a,mid+1,high)
    merge(a,low,mid,high)

def merge(a,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if a[left]<=a[right]:
            temp.append(a[left])
            left+=1
        else:
            temp.append(a[right])
            right+=1
    while left<=mid:
        temp.append(a[left])
        left += 1
    while right<=high:
        temp.append(a[right])
        right += 1
    for i in range(low,high+1):
        a[i]=temp[i-low]

if __name__=="__main__":
    n=int(input("enter size of array: "))
    a=[]
    for i in range(n):
        a.append(int(input("enter array element: ")))
    ms(a,0,len(a)-1)
    print(a)