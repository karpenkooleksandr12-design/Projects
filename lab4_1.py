import math
import sys

a = int(sys.argv[1])
h = int(sys.argv[2])
if a > 0 and h > 0:
    S = float((5 * (a**2)) / (4 * math.tan(math.pi / 5)))

    r = float(a / (2 * math.tan(math.pi / 5)))

    len = float(math.sqrt(r**2 + h**2))

    facet = float(0.5 * a * len)

    V = float((1/3) * S * h)

    print("Площа основи :" + str(S))
    print("Площа бічної грані :" + str(facet))
    print("Об'єм піраміди :" + str(V))

else:
    print("Введено неправильне число!")