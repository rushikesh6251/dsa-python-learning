if __name__ =="__main__":
    s=input("enter string")

    # pre compute
    hash1=[0]*256
    for i in range(len(s)):
        hash1[ord(s[i])]+=1
    q=int(input("enter no of queries: "))
    for i in range(q):
        c=input("enter charecter to find occurance: ")
#         fetch
        print(hash1[ord(c)])









