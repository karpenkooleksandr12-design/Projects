import random

a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

num_list = []
sq_list = []

for i in range (1,12):
    num = random.randint(a, b)
    num_list.append(num)

for i in num_list:
    sq_list.append(i ** 2)
    
print("Початковий список:", num_list)
print("Список квадратів:", sq_list)