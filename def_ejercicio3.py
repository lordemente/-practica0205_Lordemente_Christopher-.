'''llamar math para acceder a más opciones de matematicas
en este caso usaremos pi ᴨ '''
import math 

''' Formula del area de un circulo A = ᴨ*r**2''' 
def area_del_criculo(radio):
    return math.pi * radio**2

''' Formula del Volumen V = A * h''' 
def volumen_cilindro (radio, altura):
    area_base = area_del_criculo(radio)
    return area_base * altura


area = float(input("Para calcular la area de la superficie del circulo reemplace 'n': Area = ᴨ * n**2: "))
altura = float(input("Ingrese la altura del cilindro: "))

volumen =volumen_cilindro(area,altura)

print(f"superficie del circulo = {area}\nAltura del cilindro: {altura}\nResultado = {volumen:.2f} ")







    