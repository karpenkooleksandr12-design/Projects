
x = int(input("Введіть трицифрове число :"))

if x >= 100:

    num1 = x // 100
    num2 = (x // 10) % 10
    
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    
    try:
        print(num1 % num2)
    
    except:
        print("На нуль не ділиться")    

else:
    print("Ви ввели неправильне число!")