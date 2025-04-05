from trivia_logic import get_trivia

def main():
    print("¡Unéte a la Trivia de Números!")

    while True:
        try:
            num_str = input("Ingresa un número (o 'salir' para terminar): ")
            if num_str.lower() == 'salir':
                break
            num = int(num_str)
            curiosity = get_trivia(num)
            print(f"Curiosidad sobre el número {num}: {curiosity}")
        except ValueError:
            print("Por favor, ingresa un número entero válido o 'salir'.")
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()