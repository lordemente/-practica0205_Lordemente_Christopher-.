def numero_entero(numero):
   
    if numero < 0:
        return "Error"
    if numero == 0 or numero == 1:
        return 1
   
    for i in range(1, numero):
        numero = numero * i
    return numero
   
x = int(input("Introduce un número: "))
print(numero_entero(x))