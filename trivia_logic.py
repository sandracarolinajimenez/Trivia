import requests

def fetch_number_fact_from_api(num):
    """
    Obtiene una curiosidad sobre un número utilizando la API de numbersapi.com.
    """
    url = f"http://numbersapi.com/{num}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return f"Error al obtener la curiosidad para el número {num}: {e}"

# (Opcional) Si quieres mantener una versión estática para algunos números:
def fetch_number_fact_static(num):
    """
    Obtiene una curiosidad sobre un número desde un diccionario local.
    """
    trivia = {
        1: "El número 1 en tecnología digital, representa el estado «encendido» en código binario, la base de la informática.",
        2: "El número 2 es la base del logaritmo binario.",
        3: "El número 3 es un número algebraico.",
        42: "El número 42 es considerado por algunos como el significado de la vida, el universo y todo lo demás."
        # Puedes agregar más curiosidades estáticas aquí si lo deseas
    }
    return trivia.get(num)

def get_trivia(num, use_api=True):
    """
    Obtiene una curiosidad para un número, ya sea desde la API o localmente.
    """
    if not isinstance(num, int):
        raise TypeError("El argumento debe ser un número entero.")

    if use_api:
        return fetch_number_fact_from_api(num)
    else:
        static_fact = fetch_number_fact_static(num)
        if static_fact:
            return static_fact
        else:
            return fetch_number_fact_from_api(num) # Si no está localmente, intenta la API