import io
import unittest.mock
from numeros import *


class ProbarGenerador(unittest.TestCase):
    """Prueba los resultados del generador"""

    def test_generar_farmacia(self):
        next(farmacia)
        next(farmacia)
        resultado = next(farmacia)
        self.assertEqual(resultado, 'F-103')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        decorar_turno(perfumeria)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_decorar_perfumeria(self):
        self.assert_stdout(f"\n{'*' * 40}\n"
                           f"\tNº de ticket\n"
                           f"\tP-101\n"
                           f"\tEspere hasta ser atendido\n"
                           f"{'*' * 40}\n\n")
    if __name__ == '__main__':
        unittest.main()
