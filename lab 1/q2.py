k=1

l = int(input("enter number of rows: "))

for i in range(l):
    for j in range(i+1):
        print(k, end=" ")
        k=k+1
    
    print()
