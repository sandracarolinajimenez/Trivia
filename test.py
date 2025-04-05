import unittest
from trivia_logic import get_trivia  # Asegúrate de importar la función correcta

class TestTriviaLogic(unittest.TestCase):

    def test_get_trivia_valid_number_api(self):
        """Prueba que get_trivia devuelve algo (no un error genérico) para un número válido usando la API."""
        fact = get_trivia(42)
        self.assertIsNotNone(fact)
        self.assertNotEqual(fact, f"Error al obtener la curiosidad para el número 42: <built-in function get>") # Ejemplo de error que podría ocurrir

    def test_get_trivia_invalid_input(self):
        """Prueba que get_trivia levanta TypeError para una entrada no entera."""
        with self.assertRaises(TypeError):
            get_trivia("hola")

    def test_get_trivia_api_error(self):
        """
        Prueba el manejo de errores de la API (esto es más difícil de probar de forma confiable
        sin "mocking" la solicitud, pero se puede hacer una prueba básica).
        """
        fact = get_trivia(-1) # Es probable que la API no tenga información para este número y devuelva un error
        self.assertTrue(fact.startswith("Error al obtener la curiosidad para el número -1:"))

    def test_get_trivia_static_number(self):
        """Prueba que get_trivia devuelve la curiosidad estática para un número definido localmente."""
        fact = get_trivia(1, use_api=False)
        self.assertEqual(fact, "El número 1 en tecnología digital, representa el estado «encendido» en código binario, la base de la informática.")

if __name__ == '__main__':
    unittest.main()