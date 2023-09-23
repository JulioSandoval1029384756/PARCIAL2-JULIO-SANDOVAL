import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_cuadrado(lado):
    return lado**2

def main():
    figura = input("Ingrese el tipo de figura (circulo, rectangulo, triangulo, cuadrado): ").lower()
    datos = input("Ingrese los datos para calcular el área (separados por comas): ")

    datos = list(map(float, datos.split(',')))

    if figura == "circulo":
        if len(datos) == 1:
            area = calcular_area_circulo(datos[0])
            print(f"El área del círculo es: {area}")
        else:
            print("Error: El círculo requiere un solo valor (radio).")
    elif figura == "rectangulo":
        if len(datos) == 2:
            area = calcular_area_rectangulo(datos[0], datos[1])
            print(f"El área del rectángulo es: {area}")
        else:
            print("Error: El rectángulo requiere dos valores (base y altura).")
    elif figura == "triangulo":
        if len(datos) == 2:
            area = calcular_area_triangulo(datos[0], datos[1])
            print(f"El área del triángulo es: {area}")
        else:
            print("Error: El triángulo requiere dos valores (base y altura).")
    elif figura == "cuadrado":
        if len(datos) == 1:
            area = calcular_area_cuadrado(datos[0])
            print(f"El área del cuadrado es: {area}")
        else:
            print("Error: El cuadrado requiere un solo valor (lado).")
    else:
        print("Error: Figura no reconocida. Las opciones válidas son 'circulo', 'rectangulo', 'triangulo', 'cuadrado'.")

if __name__ == "__main__":
    main()
