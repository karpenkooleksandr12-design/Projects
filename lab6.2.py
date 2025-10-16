import math

def base(r):
    return math.pi * r**2


def lateral(r, h):
    return 2 * math.pi * r * h


def V(r, h):
    return base(r) * h


r = int(input("Введіть радіус основи циліндра: "))
h = int(input("Введіть висоту циліндра: "))

area_base = base(r)
area_lateral = lateral(r, h)
cylinder_v = V(r, h)

print(f"Площа основи: ", area_base)
print(f"Площа бічної поверхні: ",area_lateral)
print(f"Об’єм циліндра: ", cylinder_v)
