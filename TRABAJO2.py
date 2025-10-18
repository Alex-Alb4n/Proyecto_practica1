def clasificar_edad():
    """
    Pide la edad al usuario y clasifica si es menor, mayor o de la tercera edad.
    """
    try:
        # 1. Solicitar la edad al usuario y convertirla a número entero
        edad = int(input("Por favor, ingresa tu edad: "))

        # 2. Aplicar la lógica de clasificación
        if edad < 0:
            print("❌ Error: La edad no puede ser negativa.")
        elif edad < 18:
            print(f"Tienes {edad} años. Eres Menor de Edad. 👧")
        elif edad >= 18 and edad < 65:
            print(f"Tienes {edad} años. Eres Mayor de Edad. ✅")
        else: # edad >= 65
            print(f"Tienes {edad} años. Eres de la Tercera Edad. 👴👵")

    except ValueError:
        # Manejar el error si el usuario ingresa algo que no es un número
        print("❌ Error: Por favor, ingresa un número válido para la edad.")

# 3. Ejecutar la función principal del programa
if __name__ == "__main__":
    clasificar_edad()