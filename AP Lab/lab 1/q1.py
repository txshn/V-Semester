a=[1,2,3,4]
b=[5,6,7,8]
L=[]

for ele in a:
    if ele%2==0:
        L.append(ele)

for ele in b:
    if ele%2 !=0:
        L.append(ele)

print(L)
