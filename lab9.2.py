import numpy as np

arr = np.random.randint(0, 18, (3, 5))
num = 0
num2 = []
for i in range(3):
    for j in range(5):
        num += arr[i][j]

for i in range(3):
    for j in range(5):
        if arr[i][j] > 9:
            num2.append(arr[i][j])

print("Сума елементів масиву= ", num)
print("Елементи, більше за 9:", [int(x) for x in num2])

