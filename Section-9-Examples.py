def ac():
    global c
    c = 0
    c += 1
    return c

ac()

c+=1

print (c)

def args_func(*args):
    print (args)

args_func("hola", 400, True, 45.5)

#argumento por posicion
def suma(a, b):
    print (f"a es igua a {a} y b es igual a {b}")
    return a + b

suma(100, 500)
print (suma(100, 500))

#argumento por nombre

suma(b= 200, a = 700)
print(suma(b= 200, a = 700))

