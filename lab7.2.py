import math

a = float(input("Введіть початок діапазону: "))
b = float(input("Введіть кінець діапазону: "))
h = float(input("Введіть крок табулювання: "))


if h <= 0 or a > b or a + b < h:

    print("Введено неправильні значення")

else:

    print("\nТабулювання функції f(x) = ln|x + 11| * cos(x) + 0.27 + e:")
    
    x = a
    
    while x <= b:
        fx = math.log(abs(x + 11)) * math.cos(x) + 0.27 + math.e

        print(x, fx)
        
        x += h