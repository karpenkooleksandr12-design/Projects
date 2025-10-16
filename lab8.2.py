while True:
    try:
        N = int(input("Введіть кількість слів: "))
        if N < 0:
            print("Кількість не має бути від'ємною!")
            continue
        break
    except ValueError:
        print("Введіть ціле число.")

words = []
count = 0

for i in range(N):
    word = input("Введіть слово №" + str(i + 1) + " ")
    words.append(word)

for i in range(len(words)):

    for j in range (i + 1, len(words)):

        if len(words[i]) > 0 and len(words[j]) > 0:
            
            if words[i][0] == words[j][0]:
                count += 1

print("Кількість пар слів, що починаюься з однакових символів: ",count)