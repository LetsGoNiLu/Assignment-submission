list1 = [8, [], 3, 15, [], [], 4,[]]
print("The original list is : " + str(list1))
rests = list(filter(None, list1))
print("List after empty list removal : " + str(rests))