#squares in a dict

# squares = {1: 'Jerry', 2: 'Kwihangana', 3: 'Jeremy', 4: 'Nsabiyera'}
# print(squares)
# squares.pop(4)
# print(squares)

my_dict = {'first_name': 'Jeremiah', 'last_name': 'Kwihangana', 'course': 'Python'}
print(my_dict)

print(my_dict['first_name'])

#updating first name
my_dict['course'] = 'Blockchain'
print(my_dict)

#adding elements to the dictionary
my_dict['age'] = '22'
my_dict['marital_status'] = 'Single and happy'
print(my_dict)



# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
print(list(sorted(marks.keys())))

#Dictionary comprehension
modulus = {x: x%2==0 for x in range(40)}
print(modulus)

cubes = {x: x*x*x for x in range(10)}
print(cubes)

#Membership test in python
num_sqaured = {1:1, 2:4, 3:9, 4:16, 5:25}
print(1 in num_sqaured)
print(6 in num_sqaured)
print(2 not in num_sqaured)
print(8 not in num_sqaured)

#Iterating through a dictionary
num_sqaured = {1:1, 2:4, 3:9, 4:16, 5:25}
for i in num_sqaured:
    print(num_sqaured[i])



 # Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: False
print(all(squares))

# Output: True
print(any(squares))

# Output: 6
print(len(squares))

# Output: [0, 1, 3, 5, 7, 9]
print(sorted(squares))