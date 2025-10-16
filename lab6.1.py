import math

def first (leg1, leg2, h):

    a = math.sqrt((leg1 **2) + leg2 **2)
   
    base = 0.5 * leg1 * leg2
    
    lateral = (leg1 + leg2 + a) * h
    
    total = 2 * base + lateral

    return total

def second(leg1, leg2, h):

    base = 0.5 * leg1 * leg2
    return base * h

leg1 = int(input("Введіть перший катет: "))
leg2 = int(input("Введіть другий катет: "))
h = int(input("Введіть висоту: "))

func1 = first(leg1, leg2, h)
func2 = second(leg1, leg2, h)

print ("Повна площа поверхны призми: ", func1)
print ("Об'єм призми: ", func2)
