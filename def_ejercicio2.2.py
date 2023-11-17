def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)


numero = int(input("Introduce un número: "))
factorial = factorial_recursivo(numero)
print(f"El factorial de {numero} es: {factorial}")