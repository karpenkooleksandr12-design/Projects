import math

a = float(input("Введіть початок діапазону: "))
b = float(input("Введіть кінець діапазону: "))
h = float(input("Введіть крок табулювання: "))


if h <= 0 or a > b or a + b < h:

    print("Введено неправильні значення")

else:

    print("Табулювання функції f(x) = 4x^4 + sin(5x) - e^(-x):")

    steps = int((b - a) / h) + 1

    for i in range(steps):

        x = a + i * h
        fx = 4 * x**4 + math.sin(5 * x) - math.exp(-x)

        print("Крок №",x, fx)
