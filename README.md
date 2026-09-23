# 🚀 Aerospace Math Lab

Laboratório em Python para estudar **matemática aplicada à engenharia aeroespacial**, começando pela equação do foguete de Tsiolkovsky e evoluindo para uma simulação numérica simplificada de lançamento.

> O projeto é educacional. A simulação atual representa um lançamento vertical em 1D e não é um simulador orbital completo.

## 🎯 Objetivos

- Implementar a equação do foguete de Tsiolkovsky.
- Transformar equações físicas em código.
- Simular a evolução de altitude, velocidade, massa e aceleração ao longo do tempo.
- Praticar integração numérica com o método de Euler.
- Trabalhar com validação de parâmetros e testes automatizados.

## 🧮 Equação de Tsiolkovsky

A variação ideal de velocidade é calculada por:

**Δv = vₑ × ln(m₀ / m_f)**

| Variável | Significado | Unidade |
|---|---|---|
| Δv | Variação de velocidade | m/s |
| vₑ | Velocidade de exaustão | m/s |
| m₀ | Massa inicial | kg |
| m_f | Massa final | kg |

## 🚀 Simulação de lançamento

A simulação usa um modelo vertical simplificado. Em cada passo de tempo, o programa calcula:

- empuxo;
- massa restante;
- gravidade em função da altitude;
- aceleração;
- velocidade;
- altitude.

A integração é feita pelo **método de Euler**.

### Hipóteses do modelo

- movimento vertical unidimensional;
- empuxo constante durante a queima;
- vazão mássica constante;
- gravidade variável com a altitude;
- sem arrasto atmosférico;
- sem rotação da Terra;
- sem controle de atitude.

Essas simplificações tornam o projeto adequado para estudo de programação e matemática aplicada, mas os resultados não devem ser interpretados como uma previsão de uma missão real.

## ✨ Funcionalidades

- Cálculo de delta-v.
- Simulação numérica de lançamento.
- Evolução de altitude, velocidade, massa e aceleração.
- Validação de parâmetros físicos básicos.
- Testes automatizados com `unittest`.
- Visualização opcional com Matplotlib.

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/marcellabongiolo/aerospace-math-lab.git
cd aerospace-math-lab
```

### 2. Executar o cálculo de Tsiolkovsky

```bash
python tsiolkovsky_calculator.py
```

### 3. Executar a simulação

```bash
python launch_simulation.py
```

### 4. Gerar os gráficos da simulação

Instale a dependência de visualização:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python plot_simulation.py
```

O script gera os gráficos `altitude_tempo.png`, `velocidade_tempo.png` e `massa_tempo.png`.

### 5. Executar os testes

```bash
python -m unittest discover -s tests -v
```

## 📁 Estrutura

```text
aerospace-math-lab/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   ├── test_launch_simulation.py
│   └── test_tsiolkovsky_calculator.py
├── .gitignore
├── LICENSE
├── README.md
├── launch_simulation.py
├── plot_simulation.py
├── requirements.txt
└── tsiolkovsky_calculator.py
```

## 🧪 Conceitos praticados

- Python
- Matemática aplicada
- Equações de foguetes
- Mecânica básica
- Integração numérica
- Funções e classes
- Dataclasses
- Validação de dados
- Exceções
- Testes automatizados
- Precisão numérica
- Visualização de dados científicos

## 🔭 Próximas extensões

- Visualização com gráficos de altitude, velocidade e massa.
- Arrasto atmosférico.
- Estágios de foguete.
- Calculadora de impulso específico.
- Conversões entre unidades.
- Modelos de trajetória 2D.
- Mecânica orbital e órbitas simplificadas.

## 👩‍💻 Autora

**Marcella Bongiolo**

[GitHub](https://github.com/marcellabongiolo) · [LinkedIn](https://linkedin.com/in/marcellabongiolo)

## 📄 Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).
