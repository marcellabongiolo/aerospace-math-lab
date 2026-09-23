import unittest

from tsiolkovsky_calculator import SimuladorFoguete


class TestSimuladorFoguete(unittest.TestCase):
    def test_calcula_delta_v(self):
        resultado = SimuladorFoguete.calcular_delta_v(3000, 10_000, 2_000)

        self.assertAlmostEqual(resultado, 4_828.3137, places=3)

    def test_massa_final_zero(self):
        with self.assertRaises(ValueError):
            SimuladorFoguete.calcular_delta_v(3000, 10_000, 0)

    def test_massa_inicial_deve_ser_maior(self):
        with self.assertRaises(ValueError):
            SimuladorFoguete.calcular_delta_v(3000, 2_000, 10_000)

    def test_velocidade_de_exaustao_invalida(self):
        with self.assertRaises(ValueError):
            SimuladorFoguete.calcular_delta_v(0, 10_000, 2_000)

    def test_massa_final_negativa(self):
        with self.assertRaises(ValueError):
            SimuladorFoguete.calcular_delta_v(3000, 10_000, -1)


if __name__ == "__main__":
    unittest.main()
