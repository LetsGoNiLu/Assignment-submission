a = int(input("Enter the starting of the interval"))
b = int(input("Enter the ending of the interval"))
#i = a

for i in range(a,b,1):
    if i == 0 or i == 1:
        continue
    count = 0
    var = 2
    while var <= i/2:
       if i%var == 0:
          count = 1
       var += 1
    if count == 0:
        print(i)
    i += 1






