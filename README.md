# 🚀 Aerospace Math Lab

Laboratório em Python para estudar **matemática aplicada à engenharia aeroespacial**, começando pela equação do foguete de Tsiolkovsky.

> Este projeto é um laboratório educacional de cálculos. A implementação atual não simula uma trajetória orbital completa.

## 🎯 Objetivos

- Implementar a equação do foguete de Tsiolkovsky.
- Praticar matemática aplicada em código.
- Trabalhar com validação de entradas e exceções.
- Criar testes automatizados para cálculos científicos.
- Manter uma estrutura de projeto simples e profissional.

## 🧮 Equação de Tsiolkovsky

A variação de velocidade é calculada por:

**Δv = vₑ × ln(m₀ / m_f)**

Onde:

| Variável | Significado | Unidade |
|---|---|---|
| Δv | Variação de velocidade | m/s |
| vₑ | Velocidade de exaustão | m/s |
| m₀ | Massa inicial | kg |
| m_f | Massa final | kg |

A implementação valida se a velocidade de exaustão é positiva, se a massa final é maior que zero e se a massa inicial é maior que a massa final.

## ✨ Funcionalidades

- Cálculo de delta-v.
- Validação de parâmetros físicos básicos.
- Exemplo executável via terminal.
- Testes automatizados com `unittest`.
- Zero dependências externas.

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/marcellabongiolo/aerospace-math-lab.git
cd aerospace-math-lab
```

### 2. Executar a demonstração

```bash
python tsiolkovsky_calculator.py
```

### 3. Executar os testes

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
│   └── test_tsiolkovsky_calculator.py
├── .gitignore
├── LICENSE
├── README.md
└── tsiolkovsky_calculator.py
```

## 🧪 Conceitos praticados

- Python
- Matemática aplicada
- Equações de foguetes
- Funções e classes
- Validação de dados
- Exceções
- Testes automatizados
- Complexidade e precisão numérica

## 🔭 Próximas extensões

- Calculadora de impulso específico.
- Conversões entre unidades.
- Comparação entre diferentes estágios de foguete.
- Modelos mais completos de delta-v.
- Estudos de mecânica orbital.

## 👩‍💻 Autora

**Marcella Bongiolo**

[GitHub](https://github.com/marcellabongiolo) · [LinkedIn](https://linkedin.com/in/marcellabongiolo)

## 📄 Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).
