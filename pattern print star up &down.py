#if true print *triangle upright if false print * triangle upside down
#take number of lines from user 
print("Pattern Printer")
a= int(input("Enter \n1 to print upright \n0 to print upside down \n "))
n= int(input("Enter number of rows: "))
new = bool(a)
if new==True:
    r=1
    while r<=n:
        print(" * ",end="")
        c=1
        while c<r:
            print(" * ",end="")
            c=c+1
        r=r+1
        print()
elif new== False:
    r=1
    while r<=n:
        print(" * ",end="")
        c=r
        while c<n:
            print(" * ",end="")
            c=c+1
        r=r+1
        print()