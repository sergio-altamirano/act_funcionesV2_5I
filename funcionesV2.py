print("mas sobre funciones")
#Aqui se escribe las funciones
def suma_ab(a,b):
    s=a+b
    return s

#resta
def resta_ab(a2,b2):
    s2=a2-b2
    return s2

#multiplicacion
def mul_ab(a3,b3):
    s3=a3*b3
    return s3

#divicion
def div_ab(a4,b4):
    s4=a4/b4
    return s4

#llamadas a funciones
print("calculando suma")
n1=int(input("Ingresa el primer numero  "))
n2=int(input("Ingresa el segundo numero  "))
suma= suma_ab(n1, n2)
print(f"la suma de {n1}+{n2} es {suma}")


#resta
print("calculando resta")
n3=int(input("Ingresa el primer numero  "))
n4=int(input("Ingresa el segundo numero  "))
resta= resta_ab(n3, n4)
print(f"la suma de {n3}-{n4} es {resta}")


#multiplicacion
print("calculando multiplicacion")
n5=int(input("Ingresa el primer numero  "))
n6=int(input("Ingresa el segundo numero  "))
mul= mul_ab(n5, n6)
print(f"la multiplicacion de {n5}X{n6} es {mul}")


#divicion
print("calculando divicion")
n7=int(input("Ingresa el primer numero  "))
n8=int(input("Ingresa el segundo numero  "))
div= div_ab(n7, n8)
print(f"la suma de {n7}/{n8} es {div}")