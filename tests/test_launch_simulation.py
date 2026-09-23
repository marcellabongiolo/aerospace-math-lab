import unittest

from launch_simulation import SimuladorLancamento


class TestSimuladorLancamento(unittest.TestCase):
    def setUp(self):
        self.simulador = SimuladorLancamento(
            massa_inicial=100_000,
            massa_seca=15_000,
            empuxo=3_000_000,
            vazao_massa=3_000_000 / 3_500,
        )

    def test_simulacao_retorna_estados(self):
        estados = self.simulador.simular(duracao=10, passo=1)

        self.assertEqual(len(estados), 11)
        self.assertEqual(estados[0].altitude, 0)
        self.assertEqual(estados[0].velocidade, 0)

    def test_massa_nao_fica_abaixo_da_massa_seca(self):
        estados = self.simulador.simular(duracao=120, passo=0.1)

        self.assertGreaterEqual(min(e.massa for e in estados), 15_000)

    def test_altitude_aumenta_com_empuxo_suficiente(self):
        estados = self.simulador.simular(duracao=10, passo=0.1)

        self.assertGreater(estados[-1].altitude, 0)
        self.assertGreater(estados[-1].velocidade, 0)

    def test_parametros_invalidos(self):
        with self.assertRaises(ValueError):
            SimuladorLancamento(0, 15_000, 3_000_000, 800)

        with self.assertRaises(ValueError):
            SimuladorLancamento(100_000, 100_000, 3_000_000, 800)

        with self.assertRaises(ValueError):
            self.simulador.simular(duracao=0)


if __name__ == "__main__":
    unittest.main()
