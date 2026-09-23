"""Gera gráficos da simulação de lançamento.

Requer matplotlib. Execute:
    python plot_simulation.py
"""

import matplotlib.pyplot as plt

from launch_simulation import SimuladorLancamento


def main() -> None:
    simulador = SimuladorLancamento(
        massa_inicial=100_000.0,
        massa_seca=15_000.0,
        empuxo=3_000_000.0,
        vazao_massa=3_000_000.0 / 3_500.0,
    )
    estados = simulador.simular(duracao=120.0, passo=0.1)

    tempo = [estado.tempo for estado in estados]
    altitude = [estado.altitude / 1000 for estado in estados]
    velocidade = [estado.velocidade / 1000 for estado in estados]
    massa = [estado.massa / 1000 for estado in estados]

    fig, ax = plt.subplots()
    ax.plot(tempo, altitude)
    ax.set_title("Altitude durante o lançamento")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Altitude (km)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("altitude_tempo.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.plot(tempo, velocidade)
    ax.set_title("Velocidade durante o lançamento")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Velocidade (km/s)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("velocidade_tempo.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.plot(tempo, massa)
    ax.set_title("Massa do foguete durante o lançamento")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Massa (toneladas)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("massa_tempo.png", dpi=150)
    plt.close(fig)

    print("Gráficos gerados:")
    print("- altitude_tempo.png")
    print("- velocidade_tempo.png")
    print("- massa_tempo.png")


if __name__ == "__main__":
    main()
