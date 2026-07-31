def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("a =", a)
    print("b =", b)

a = 10
b = 20

swap(a, b)
