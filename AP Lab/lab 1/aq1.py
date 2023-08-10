n=int(input("enter first number: "))
m=int(input("enter second number: "))

for num in range(n, m):
    if num>1:
        for k in range(2, int(pow(num, 0.5))):
            if (num%k) == 0:
                break
        else:
            print(num)
