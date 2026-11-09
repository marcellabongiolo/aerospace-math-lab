import unittest
from unittest.mock import patch

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

    def test_simulacao_para_ao_tocar_o_solo(self):
        simulador = SimuladorLancamento(
            massa_inicial=10_000,
            massa_seca=9_000,
            empuxo=1,
            vazao_massa=0.1,
        )

        estados = simulador.simular(duracao=120, passo=0.1)

        self.assertEqual(estados[-1].altitude, 0.0)
        self.assertEqual(estados[-1].velocidade, 0.0)

    def test_parametros_invalidos(self):
        with self.assertRaises(ValueError):
            SimuladorLancamento(0, 15_000, 3_000_000, 800)

        with self.assertRaises(ValueError):
            SimuladorLancamento(100_000, 100_000, 3_000_000, 800)

        with self.assertRaises(ValueError):
            self.simulador.simular(duracao=0)

    def test_corta_passo_no_fim_do_combustivel(self):
        simulador = SimuladorLancamento(10, 9, 100, 10)
        with patch.object(SimuladorLancamento, "gravidade", return_value=0.0):
            estados = simulador.simular(duracao=1, passo=1)
        self.assertAlmostEqual(estados[1].tempo, 0.1)
        self.assertAlmostEqual(estados[-1].velocidade, 1.0)
        self.assertEqual(estados[-1].massa, 9)
        self.assertAlmostEqual(estados[-1].tempo, 1.0)

    def test_rejeita_parametros_nao_finitos(self):
        for valor in (float("nan"), float("inf"), float("-inf")):
            for indice in range(4):
                parametros = [100_000, 15_000, 3_000_000, 800]
                parametros[indice] = valor
                with self.subTest(indice=indice, valor=valor), self.assertRaises(ValueError):
                    SimuladorLancamento(*parametros)
            with self.assertRaises(ValueError):
                self.simulador.simular(duracao=valor)
            with self.assertRaises(ValueError):
                self.simulador.simular(passo=valor)

    def test_reduzir_passo_aproxima_altitude_de_referencia(self):
        referencia = self.simulador.simular(duracao=10, passo=0.0625)[-1].altitude
        erros = [
            abs(self.simulador.simular(duracao=10, passo=passo)[-1].altitude - referencia)
            for passo in (1.0, 0.5, 0.25)
        ]
        self.assertGreater(erros[0], erros[1])
        self.assertGreater(erros[1], erros[2])


if __name__ == "__main__":
    unittest.main()
