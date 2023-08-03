n = int(input("enter your number: "))

su=0
temp=n

while temp>0:
    digit=temp%10
    su = su + digit**len(str(n))
    temp = temp//10

if n==su:
    print("armstrong ")

else:
    print("not armstrong ")
