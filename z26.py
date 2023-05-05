a = int(input("Введите число: "))
b = int(input("Введите степень: "))

def step(a, b):
    if b == 0:
        return 1
    return a * step(a, b - 1)

print(step(a, b))