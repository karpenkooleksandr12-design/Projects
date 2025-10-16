l1 = input("Введіть перший рядок слів: ")
l2 = input("Введіть другий рядок слів: ")

words = (l1 + " " + l2).split()

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if len(words[i]) < len(words[j]):
            words[i], words[j] = words[j], words[i]

print("Слова в порядку зменшення довжини")
for word in words:
    print(word)