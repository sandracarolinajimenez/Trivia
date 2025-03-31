import unittest
from main import trivia_fetch

class TestTriviaFetch(unittest.TestCase):

    def test_valid_number(self):
        self.assertEqual(trivia_fetch(1), "El número 1 en tecnología digital, representa el estado «encendido» en código binario, la base de la informática.")
        self.assertEqual(trivia_fetch(2), "El número 2 es la base del logaritmo binario.")
        self.assertEqual(trivia_fetch(3), "El número 3 es un número algebraico.")

    def test_invalid_number(self):
        self.assertEqual(trivia_fetch(10), "Lo siento, no hay información sobre este número.")

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            trivia_fetch("a")

if __name__ == "__main__":
    unittest.main()