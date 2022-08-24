#No.1 sum of the items in the list

size = int(input("The size of the list is? "))
sum = [x + x for x in range(size) ]
print(sum)


#No.2

list = ['abc', 'xyz', 'aba', '1221']
print(list.count('1221')) 


#No.3 

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
del fruits[1]
del fruits[2]
del fruits[3]
print(fruits)

#No. 4

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list.pop(0)
list.pop(3)
list.pop(3)
print(list)

#No. 5

square = sqrt(x)
numbers = [sqrt(x) for x in range(1,31)]
if numbers.index()>4:
    
    print(square)

