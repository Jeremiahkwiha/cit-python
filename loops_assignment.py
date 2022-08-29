#No.1
n = 1
while n <= 10:
    print(n)
    n += 1


#No. 2

n = int(input("Enter number\n"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of numbers is: ", sum)  


#No.3
num = 2
print("Multiplication Table of", num)
for i in range(1, 10):
   print(num,"X",i,"=",num * i)

#No.5

num = 4673453
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))


#No.6
n=-10
while n<=-1:
    print(n)
    n=n + 1


#No.4
num = [12, 75, 150, 180, 145, 525, 50]
n = []
for i in num:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        n.append(i)
        
print(n)