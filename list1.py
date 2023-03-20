#list1 = [1, 2, 3, 4, 5]
list2 = ['Ney', 'Leo', 'Erling', 'Phil', 'Jude']
#list3 = ['yoo', 1, True, 219.189, -9]

#print(list1[2])
#print(*list1)
#print(*list3)
print(*list2)

# print(list2, sep= " ")
list2.insert(len(list2), 'Travis')
print(list2, sep= " ")
list2.insert(0, 'Pep')
print(list2, sep= " ")
list2.append('Jack')
print(list2, sep= " ")