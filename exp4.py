list1=[1,2,3,4,5,6,7,8]
list2=["Aayan","jiya","Roshani","stan","eminem"]
list3=[]
# print(list1*3)
# print(list1+list2)
# print(7 in list1)
# print("lilwayne" in list2)
# print(len(list1))
# print(len(list2))
# print(max(list1))
# print(min(list2))

list1.append(9)
print(list1)
list3=list1.copy()
print(list3)
print(list1.count(7))
list2.extend("way")
print(list2)
print(list1.index(5))

list1.insert(5,"BRO")
print(list1)
list1.pop(6)
print(list1)
list2.remove("eminem")
print(list2)
list1.reverse()
print(list1)

list1.sort()
print(list1)








