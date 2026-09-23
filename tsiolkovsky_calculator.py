"""
Módulo: Simulador da Equação do Foguete (Tsiolkovsky)
Autor: Marcella Bongiolo
Descrição: Calcula a variação de velocidade (Delta-v) necessária e 
           alcançada por um foguete com base na física de propulsão.
"""

import math

class SimuladorFoguete:
    """Implementa cálculos fundamentais de engenharia aeroespacial."""
    
    @staticmethod
    def calcular_delta_v(velocidade_exaustao: float, massa_inicial: float, massa_final: float) -> float:
        """
        Calcula o Delta-v (mudança de velocidade) usando a Equação do Foguete de Tsiolkovsky:
        Delta_v = v_e * ln(m_0 / m_f)
        """
        if massa_final <= 0 or massa_inicial <= massa_final:
            raise ValueError("A massa final deve ser maior que zero e menor que a massa inicial.")
        
        delta_v = velocidade_exaustao * math.log(massa_inicial / massa_final)
        return delta_v

def main():
    print("=" * 60)
    print(" 🚀 AEROSPACE MATH LAB: EQUAÇÃO DE TSIOLKOVSKY 🌌")
    print("=" * 60)

    # Exemplo simulando parâmetros de um estágio de foguete
    # v_e: Velocidade de exaustão do motor (ex: motor Raptor da SpaceX usa aprox 3000 m/s a 3800 m/s)
    vel_exaustao = 3500.0  # metros por segundo (m/s)
    massa_total_inicial = 100000.0  # kg (foguete + combustível cheio)
    massa_seca_final = 15000.0      # kg (foguete vazio, sem propelente)

    print(f"\nParâmetros da Simulação:")
    print(f"🔹 Velocidade de Exaustão (v_e): {vel_exaustao} m/s")
    print(f"🔹 Massa Inicial (Combustível Cheio): {massa_total_inicial} kg")
    print(f"🔹 Massa Final (Foguete Vazio): {massa_seca_final} kg")

    try:
        delta_v_obtido = SimuladorFoguete.calcular_delta_v(vel_exaustao, massa_total_inicial, massa_seca_final)
        print(f"\n🎯 Resultado do Delta-v calculado:")
        print(f"✨ Delta-v: {delta_v_obtido:.2f} m/s ({delta_v_obtido / 1000:.2f} km/s)")
        print(f"💡 Informação: Para escapar da gravidade da Terra e atingir órbita baixa (LEO),")
        print(f"   geralmente precisamos de um Delta-v total de cerca de 9.3 a 10 km/s.")
    except ValueError as e:
        print(f"⚠️ Erro no cálculo: {e}")

    print("=" * 60)

if __name__ == "__main__":
    main()
  Add Tsiolkovsky rocket equation calculator
