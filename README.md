# CP4 - Dynamic Programming

## Rota Inteligente Brasil

### Introdução

A logística de transporte envolve diversas decisões estratégicas, como escolher rotas eficientes, reduzir custos e minimizar riscos durante o deslocamento de cargas. Este projeto apresenta uma solução computacional que simula esse tipo de tomada de decisão utilizando algoritmos clássicos da ciência da computação.

A proposta consiste em representar uma rede de transporte entre cidades brasileiras por meio de um **grafo**, permitindo analisar diferentes caminhos possíveis entre uma origem e um destino. A partir dessa modelagem, o sistema aplica algoritmos para identificar rotas eficientes considerando fatores logísticos relevantes.

---

### Representação do Problema

Para estruturar o sistema, a rede logística foi modelada da seguinte forma:

- **Cidades** são representadas como **nós do grafo**
- **Conexões entre cidades** representam **rotas de transporte**
- Cada rota possui um **peso**, que representa o custo associado ao trajeto

O custo de cada rota é calculado levando em conta três fatores principais:

```
custo_total = custo_reais + (risco_atraso * peso) + (perda_percentual * peso)
```

Essa abordagem permite que o algoritmo avalie não apenas o custo financeiro, mas também possíveis riscos envolvidos no transporte.

---

### Técnicas Algorítmicas Utilizadas

Para analisar as rotas disponíveis, foram aplicadas três abordagens diferentes.

#### Dijkstra

O algoritmo de Dijkstra é utilizado para encontrar o **menor custo entre duas cidades** dentro da rede. Ele percorre os caminhos possíveis acumulando os custos e garantindo a escolha da rota mais eficiente.

#### Guloso (Greedy)

A estratégia gulosa seleciona sempre a **melhor alternativa imediata**, escolhendo a rota com menor custo naquele momento. Embora seja uma abordagem rápida, ela pode não encontrar a solução global ideal em alguns cenários.

#### Programação Dinâmica

A Programação Dinâmica foi aplicada para melhorar o processo de **distribuição e alocação de carga**, evitando cálculos repetidos por meio de **memoização**. Para isso, foi utilizado o recurso `lru_cache`, que armazena resultados intermediários e melhora o desempenho da execução.

---

### Organização do Projeto

A estrutura do repositório foi organizada para separar dados, implementação e testes:

```
project/
│
├── data/          # arquivos de dados utilizados nos cenários
├── src/           # implementação dos algoritmos
├── tests/         # testes automatizados
├── notebooks/     # análises e visualizações
│
├── main.py
└── requirements.txt
```

---

### Execução do Projeto

Para rodar o sistema localmente, siga os passos abaixo.

**Instalar dependências**

```
pip install -r requirements.txt
```

**Executar o programa**

```
python main.py
```

**Rodar testes automatizados**

```
python -m pytest
```

---

### Simulação

O projeto inclui três conjuntos de dados que representam diferentes regiões logísticas do Brasil.

- **Cenário A** – cidades do interior de São Paulo e Minas Gerais  
- **Cenário B** – rotas do Centro-Oeste com destino ao Porto de Santos  
- **Cenário C** – cidades localizadas na região Nordeste  

Durante a execução do programa, o usuário pode selecionar o cenário desejado

#### Exemplos

Após selecionar o cenário e definir origem e destino, o sistema apresenta os caminhos encontrados pelos algoritmos.

```
Cenário: A
Origem: Ribeirao_Preto
Destino: Belo_Horizonte

Dijkstra: ['Ribeirao_Preto', 'Campinas', 'Belo_Horizonte']
Greedy: {'cost': ..., 'path': [...]}
DP: ...
```

---

### Visualização dos Dados

Para auxiliar na interpretação dos resultados, o projeto utiliza algumas formas de visualização, com gráficos e análise entre algoritmos.

---

### Limitações

Apesar de demonstrar diferentes estratégias de otimização, o projeto possui algumas limitações:

- As coordenadas utilizadas nos mapas não são exatas
- O algoritmo guloso pode produzir soluções abaixo do nível ideal
- A DP foi aplicada apenas na etapa de alocação de carga

---

### Considerações Finais

A utilização de diferentes algoritmos permite comparar estratégias distintas para resolver problemas logísticos. Enquanto alguns métodos priorizam velocidade de execução, outros buscam garantir a solução mais eficiente possível. Essa análise evidencia como técnicas computacionais podem apoiar decisões em cenários reais de transporte e distribuição.

---

### Integrantes

Maria Eduarda Ferrés — RM 560418  
Gabriela Queiroga Cocuzza da Silva — RM 560035
