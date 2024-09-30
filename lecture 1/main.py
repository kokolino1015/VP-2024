# print('hello world')
# str
# int
# float
# age = int(input())
# print(f"Age {age}")
# print("Age" + str(age))
# name = input()
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(f"num1 = {num1}, num2 = {num2:.2f}, num3 = {num3}")
# print(name.upper())
# print(name.lower())
# print(name.capitalize())

data = []
[a for a in range(1,9) if a % 2 == 0]
for a in range(0, 9):
    data.append(a)
print(data)
for a in range(0, 9):
    print(a, end=' ')

for i in range(10, 0, -1):
    data.insert(0, i)