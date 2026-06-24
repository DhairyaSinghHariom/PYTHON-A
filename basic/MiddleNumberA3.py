a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if (a > b and a < c) or (a < b and a > c):
    print("Middle number is:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Middle number is:", b)
else:
    print("Middle number is:", c)
