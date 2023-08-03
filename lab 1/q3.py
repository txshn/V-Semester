n=int(input("enter number of strings: "))

b=[]
count=0


for i in range(n):
    a=input()
    b.append(a)
    if len(a)%2!=0:
        print(a)

    if a[0]==a[-1] or len(a)>2:
        count+=1

print(b)
print(count)

