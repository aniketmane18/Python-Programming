n = int(input("Enter number :"))
flag = False
for i in range(2,n):
    if n % i == 0:
        flag = True
        break
if not(flag):
    print(n,"is Prime")
else:
    print(n,"Not Prime")