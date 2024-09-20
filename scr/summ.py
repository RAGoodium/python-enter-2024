n = int(input("Enter the amount of numbers: "))
p = 0
d = 0

for i in range(n):
    num = int(input())
    if num >= 0:
        p = p + num
    else:
        d = d + num
print("amount:", n)
print("plus:", p)
print("minus:", d)