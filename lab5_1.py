import math

#V = (4/ 3) * math.pi

x = input("Введіть діаметр конуса: ")
h = input("Введіть висоту конуса: ")
a1 = input("Введіть першу сторону основи піраміди: ")
a2 = input("Введіть другу сторону основи піраміди: ")
hpir = input("Введіть висоту піраміди: ")

R = int(x)/2

Vkon = float((1/3) * math.pi * (R **2) * h)
l = float(math.sqrt((R **2) + h**2))
Skon = float(math.pi * (R **2) + math.pi * R * l)

Vpir = float((1/3) * (a1 * a2) * hpir)
h1 = float(math.sqrt(hpir **2 + (a1/2)**2))
h2 = float(math.sqrt(hpir **2 + (a2/2)**2))
Spir = float(a1 * a2 + a1 * h1 + a2 * h2)

print("Об'єм конуса: " + str(Vkon))
print("Об'єм піраміди: "+ str(Vpir))

if Vkon > Vpir:
    print("Об'єм конуса більший")
else:
    print("Об'єм піраміди більший")

print("Площа поверхні конуса: " + str(Skon))
print("Площа поверхні піраміди" + str(Spir))

if Skon > Spir:
    print("Площа конуса більша")
else:
    print("Площа піраміди більша")
