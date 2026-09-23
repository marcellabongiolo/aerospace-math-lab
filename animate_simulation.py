"""Anima a simulação de lançamento vertical.

Requer matplotlib. Execute:
    python animate_simulation.py

A animação mostra, ao longo do tempo:
- altitude do foguete;
- velocidade;
- massa restante.
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    ax.set_title("Simulação de lançamento vertical")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Altitude (km)")

    linha_altitude, = ax.plot([], [], linewidth=2)
    ponto_foguete, = ax.plot([], [], marker="o")
    texto = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

    ax.set_xlim(0, tempo[-1])
    margem = max(10.0, max(altitude) * 0.05)
    ax.set_ylim(0, max(altitude) + margem)
    ax.grid(True, alpha=0.3)

    def atualizar(indice: int):
        linha_altitude.set_data(tempo[: indice + 1], altitude[: indice + 1])
        ponto_foguete.set_data([tempo[indice]], [altitude[indice]])
        texto.set_text(
            f"t = {tempo[indice]:.1f} s\n"
            f"Altitude = {altitude[indice]:.2f} km\n"
            f"Velocidade = {velocidade[indice]:.2f} km/s\n"
            f"Massa = {massa[indice]:.1f} t"
        )
        return linha_altitude, ponto_foguete, texto

    animacao = FuncAnimation(
        fig,
        atualizar,
        frames=len(estados),
        interval=20,
        blit=True,
        repeat=False,
    )

    plt.show()
    _ = animacao


if __name__ == "__main__":
    main()
