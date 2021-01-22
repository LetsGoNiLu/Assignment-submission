count = int(input("Enter the quantity of numbers you want to insert"))
sum = 0
i=1
while i<=count:
    n = int(input("Enter the number"))
    sum = sum + n
    i+=1
print("Sum of the numbers is", sum)