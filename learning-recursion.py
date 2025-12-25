def f():
    # this shows infinite recursion
    print("1")
    f()
if __name__=="__main__":
    f()