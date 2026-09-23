"""Simulação numérica simplificada de um lançamento vertical.

O modelo usa integração de Euler para acompanhar altitude, velocidade,
massa e aceleração durante a queima de combustível.

Hipóteses:
- movimento vertical unidimensional;
- empuxo constante durante a queima;
- vazão mássica constante;
- gravidade variável com a altitude;
- sem arrasto atmosférico;
- sem rotação da Terra;
- sem controle de atitude.

O objetivo é educacional: demonstrar como equações físicas podem ser
transformadas em uma simulação computacional.
"""

from dataclasses import dataclass

RAIO_TERRA_M = 6_371_000.0
GRAVIDADE_SUPERFICIE = 9.80665


@dataclass(frozen=True)
class EstadoSimulacao:
    """Representa o estado do foguete em um instante."""

    tempo: float
    altitude: float
    velocidade: float
    massa: float
    aceleracao: float


class SimuladorLancamento:
    """Simula um lançamento vertical com um modelo simplificado."""

    def __init__(
        self,
        massa_inicial: float,
        massa_seca: float,
        empuxo: float,
        vazao_massa: float,
    ) -> None:
        if massa_inicial <= 0:
            raise ValueError("A massa inicial deve ser maior que zero.")
        if massa_seca <= 0 or massa_seca >= massa_inicial:
            raise ValueError(
                "A massa seca deve ser maior que zero e menor que a massa inicial."
            )
        if empuxo <= 0:
            raise ValueError("O empuxo deve ser maior que zero.")
        if vazao_massa <= 0:
            raise ValueError("A vazão de massa deve ser maior que zero.")

        self.massa_inicial = massa_inicial
        self.massa_seca = massa_seca
        self.empuxo = empuxo
        self.vazao_massa = vazao_massa

    @staticmethod
    def gravidade(altitude: float) -> float:
        """Calcula a gravidade aproximada em função da altitude."""
        raio = RAIO_TERRA_M + max(altitude, 0.0)
        return GRAVIDADE_SUPERFICIE * (RAIO_TERRA_M / raio) ** 2

    def simular(
        self,
        duracao: float = 120.0,
        passo: float = 0.1,
    ) -> list[EstadoSimulacao]:
        """Executa a simulação e retorna os estados calculados."""
        if duracao <= 0:
            raise ValueError("A duração deve ser maior que zero.")
        if passo <= 0:
            raise ValueError("O passo de integração deve ser maior que zero.")

        estados: list[EstadoSimulacao] = []
        tempo = 0.0
        altitude = 0.0
        velocidade = 0.0
        massa = self.massa_inicial

        while tempo <= duracao + 1e-9:
            gravidade = self.gravidade(altitude)
            combustivel = massa > self.massa_seca
            empuxo_atual = self.empuxo if combustivel else 0.0
            aceleracao = empuxo_atual / massa - gravidade

            estados.append(
                EstadoSimulacao(
                    tempo=tempo,
                    altitude=altitude,
                    velocidade=velocidade,
                    massa=massa,
                    aceleracao=aceleracao,
                )
            )

            dt = min(passo, duracao - tempo)
            if dt <= 0:
                break

            if combustivel:
                massa_nova = max(
                    self.massa_seca,
                    massa - self.vazao_massa * dt,
                )
            else:
                massa_nova = massa

            velocidade_nova = velocidade + aceleracao * dt
            altitude_nova = altitude + velocidade_nova * dt

            if altitude_nova <= 0 and velocidade_nova < 0 and tempo > 0:
                altitude = 0.0
                velocidade = 0.0
                massa = massa_nova
                tempo += dt
                estados.append(
                    EstadoSimulacao(
                        tempo=tempo,
                        altitude=altitude,
                        velocidade=velocidade,
                        massa=massa,
                        aceleracao=aceleracao,
                    )
                )
                break

            velocidade = velocidade_nova
            altitude = max(0.0, altitude_nova)
            massa = massa_nova
            tempo += dt

        return estados


def main() -> None:
    """Executa um cenário demonstrativo de lançamento vertical."""
    simulador = SimuladorLancamento(
        massa_inicial=100_000.0,
        massa_seca=15_000.0,
        empuxo=3_000_000.0,
        vazao_massa=3_000_000.0 / 3_500.0,
    )

    estados = simulador.simular(duracao=120.0, passo=0.1)
    final = estados[-1]
    maior_altitude = max(estados, key=lambda estado: estado.altitude)

    print("=" * 64)
    print("🚀 AEROSPACE MATH LAB: SIMULAÇÃO DE LANÇAMENTO")
    print("=" * 64)
    print("Modelo: movimento vertical 1D, sem arrasto atmosférico.")
    print(f"Tempo final: {final.tempo:.1f} s")
    print(f"Altitude final: {final.altitude / 1000:.2f} km")
    print(f"Velocidade final: {final.velocidade / 1000:.2f} km/s")
    print(f"Altitude máxima: {maior_altitude.altitude / 1000:.2f} km")
    print(f"Massa final: {final.massa:.0f} kg")
    print("=" * 64)


if __name__ == "__main__":
    main()
