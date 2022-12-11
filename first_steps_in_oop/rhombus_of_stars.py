
n = int(input())

for row in range(1,n+1):
    for space in range(1,n-(row - 1)):
        print(" ",end =" ")
    for star in range(1,row+1):
        print("*",end =" ")
    print()

for row in range(n-1,0,-1):
    for star in range(1,row+1):
        print(" ",end =" ")
    for star in range(1,row+1):
        print("*",end =" ")
    print()

