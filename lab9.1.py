import numpy as np

arr = np.random.randint(1, 21, size=11)
print("Початковий масив: ", arr)

values, counts = np.unique(arr, return_counts=True)
most_common = values[counts.argmax()]
print("Найчастіше число:", most_common)

arr = np.delete(arr, 0)
print("Після видалення першого елемента:", arr)

new_num = np.random.randint(0, 40)
arr = np.append(arr, new_num)

print("Додаємо в кінець число:", new_num)
print("Оновлений масив:", arr)