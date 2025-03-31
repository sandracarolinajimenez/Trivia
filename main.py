def trivia_fetch(num):
    # Esta función da un número y debe darte una curiosidad 
    if not isinstance(num, int):
        raise TypeError("El argumento debe ser un número entero.")
    
    trivia = {
        1: "El número 1 en tecnología digital, representa el estado «encendido» en código binario, la base de la informática.",
        2: "El número 2 es la base del logaritmo binario.",
        3: "El número 3 es un número algebraico."
    }
    return trivia.get(num, "Lo siento, no hay información sobre este número.")

def main():
    print("¡Unéte a la Trivia de Números!")
    
    # Obtener un número del usuario
    try:
        num = int(input("Ingresa un número, del 1 al 3, para saber una curiosidad sobre él: "))
        result = trivia_fetch(num)
        print(f"Curiosidad: {result}")
    except ValueError:
        print("Por favor, ingresa un número válido.")
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()