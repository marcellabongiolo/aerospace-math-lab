"""Cálculo da equação do foguete de Tsiolkovsky.

O módulo calcula o delta-v de um estágio de foguete a partir da
velocidade de exaustão e das massas inicial e final.
"""

import math


class SimuladorFoguete:
    """Implementa o cálculo da equação do foguete de Tsiolkovsky."""

    @staticmethod
    def calcular_delta_v(
        velocidade_exaustao: float,
        massa_inicial: float,
        massa_final: float,
    ) -> float:
        """Calcula o delta-v em m/s.

        Fórmula:
            Δv = v_e * ln(m_0 / m_f)
        """
        if velocidade_exaustao <= 0:
            raise ValueError("A velocidade de exaustão deve ser maior que zero.")
        if massa_final <= 0:
            raise ValueError("A massa final deve ser maior que zero.")
        if massa_inicial <= massa_final:
            raise ValueError(
                "A massa inicial deve ser maior que a massa final."
            )

        return velocidade_exaustao * math.log(massa_inicial / massa_final)


def main() -> None:
    """Executa um exemplo de cálculo para um estágio de foguete."""
    print("=" * 60)
    print("🚀 AEROSPACE MATH LAB: EQUAÇÃO DE TSIOLKOVSKY 🌌")
    print("=" * 60)

    velocidade_exaustao = 3500.0
    massa_inicial = 100_000.0
    massa_final = 15_000.0

    print("\nParâmetros da simulação:")
    print(f"🔹 Velocidade de exaustão: {velocidade_exaustao:.0f} m/s")
    print(f"🔹 Massa inicial: {massa_inicial:.0f} kg")
    print(f"🔹 Massa final: {massa_final:.0f} kg")

    delta_v = SimuladorFoguete.calcular_delta_v(
        velocidade_exaustao,
        massa_inicial,
        massa_final,
    )

    print("\n🎯 Resultado:")
    print(f"✨ Delta-v: {delta_v:.2f} m/s ({delta_v / 1000:.2f} km/s)")
    print("=" * 60)


if __name__ == "__main__":
    main()
