# Relatório Técnico Karatsuba
## Sobre o projeto
Trabalho realizado para a disciplina de FPAA (Fundamentos de Projeto e Análise de Algoritmos) do curso de Engenharia de Software (PUC Minas). O objetivo do trabalho é implementar o algoritmo de multiplicação de inteiros Karatsuba e realizar uma análise de complexidade do mesmo.

## Algoritmo de Karatsuba

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números
inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a
complexidade da multiplicação em comparação ao método tradicional de
multiplicação direta.

### Explicação linha a linha do código

```python
def karatsuba(x: int, y: int) -> int:
 if x < 10 or y < 10:
     return x * y
 else:
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    a = x // (10 ** (half)) #Left part of x
    b= x % (10 ** (half)) # Right part of x
    c = y // (10 ** (half)) # Left part of y
    d = y % (10 ** (half)) # Right part of y
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd
```


## Como execurtar o projeto


## Relatório Técnico

### Análise de Complexidade Ciclomática

#### O que é Complexidade Ciclomática?

A complexidade ciclomática é uma métrica usada para medir a complexidade do fluxo de controle de um programa. Ela calcula o número de caminhos independentes no código, considerando estruturas como loops (`for`, `while`) e condicionais (`if`, `try/except`). Quanto maior o valor, mais complexo é o código.

**Fórmula:**  
\(
M = E - N + 2P
\)  

Onde:  
- \(M\): Complexidade Ciclomática  
- \(E\): Número de arestas (transições) no grafo do controle de fluxo  
- \(N\): Número de nós (blocos de código)  
- \(P\): Componentes conectados (geralmente 1 para programas simples)  


### Análise de Complexidade Assintótica
