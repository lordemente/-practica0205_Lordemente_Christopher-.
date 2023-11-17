'''Formula = ∑número / longitud de total de número'''


def calcular_media_desde_input():
    lista = input("Ingresa los números separados por espacios: ")
    numeros = [float(x) for x in lista.split()]  # Convierte la entrada en una lista de números
    print(numeros)

    if len(numeros) == 0:
        return 0
    else:
        return sum(numeros) / len(numeros)

''' Llamamos nuestra función en una variable '''
media = calcular_media_desde_input()
print(f"La media de los números ingresados es: {media:.2f}")

