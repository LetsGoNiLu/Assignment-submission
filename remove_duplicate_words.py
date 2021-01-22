from collections import Counter
x = input("Enter the string")
x = x.split(" ")
for i in range(0, len(x)):
    x[i] = "".join(x[i])

count = Counter(x)

str = " ".join(count.keys())
print(str)