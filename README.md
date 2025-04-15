
# Sistema de Controle de Estacionamento & Análise de Produtos

## Descrição do Projeto

Este repositório contém dois projetos complementares:

1. **Sistema de Controle de Estacionamento** (Projeto acadêmico de Algoritmos e Programação I - Universidade Presbiteriana Mackenzie), que simula um sistema completo de controle de entrada, saída e cobrança de veículos em um estacionamento.
2. **Analisador de Dados de Produtos (`emack.csv`)**, desenvolvido em Python, que realiza estatísticas e relatórios HTML com base em um dataset de produtos e categorias.

---

## Sistema de Estacionamento

### Funcionalidades:

- **Cadastro de Tarifas**
  - Tarifas específicas para **carros pequenos, grandes** e **motos**, com valores para até 3h e adicionais.
  - Permite alterações das tarifas a qualquer momento.

- **Controle de Entrada e Saída**
  - Registro de entrada com placa, tipo de veículo, data e hora.
  - Registro de saída com cálculo automático de tempo, tarifa e desconto de 5% para pagamentos via PIX.
  - Geração automática de recibos de entrada e saída.

- **Relatórios**
  - Relatório diário com:
    - Quantidade de entradas/saídas.
    - Tempo médio de permanência.
    - Total arrecadado.
  - Relatório por tipo de veículo com média de gastos e frequência.

### Menu Principal:
```
1. Cadastrar Tarifas
2. Registrar Entrada de Veículo
3. Registrar Saída de Veículo
4. Gerar Relatório diário
5. Gerar Relatório por tipo de veículo
6. Sair
```

---

## Analisador de Produtos com Python

### Dataset: `emack.csv`

Contém uma base de produtos estruturada com os seguintes campos principais:

- `id`: Identificador único
- `title`: Nome do produto
- `categoryName`: Categoria (ex: Livros, Moda, Esportes, Eletrônicos, Casa)
- `price`: Preço do produto
- `boughtInLastMonth`: Quantidade vendida no último mês
- `isBestSeller`: Flag de produto mais vendido

### Funcionalidades do Script `gerar_relatorio_html.py`

- **Contagem de Produtos por Categoria**
- **Percentual de Produtos por Categoria**
- **Proporção de Produtos Best-Sellers por Categoria**
- **Top 10 Produtos Mais Caros e Mais Baratos**
- **Listagem de Produtos por Categoria**
- **Geração de Relatório HTML de Best-Sellers por Categoria**
- **Geração de Relatório HTML de Produtos por Categoria Escolhida**

---
