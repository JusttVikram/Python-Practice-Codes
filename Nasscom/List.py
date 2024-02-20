list1 = [1,2,3,4,5]
list2 = ['Apple', 'Banana', 'Cherry']
list3 = [3.45, 'Vinod', 'Jasmine', 20]
list4= [3,2,4,6,7,9,1]

#indexing
print(list1[2])

#slicing
print(list3[::-1])
print(list2[0:2])

#length
print(len(list3))

#append
print(list2)

#sorting
list4.sort()
print(list4)

#insert and remove
list2.insert(2,'Yash')
list2.remove('Yash')
print(list2)

#pop
print(list2.pop(1))

#extend
list1.extend([77,55,44,33.99])
list1.sort()
print(list1)

#nested lists
list5 = [[list1],[list2]]
print(list5)
