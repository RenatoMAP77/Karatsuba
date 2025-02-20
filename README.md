# Relatório Técnico Karatsuba
## Sobre o projeto
Trabalho realizado para a disciplina de FPAA (Fundamentos de Projeto e Análise de Algoritmos) do curso de Engenharia de Software (PUC Minas). O objetivo do trabalho é implementar o algoritmo de multiplicação de inteiros Karatsuba e realizar uma análise de complexidade do mesmo.

## Algoritmo de Karatsuba

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números
inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a
complexidade da multiplicação em comparação ao método tradicional de
multiplicação direta.

### Explicação do Algoritmo
O algoritmo de Karatsuba funciona com base na abordagem "divide and conquer", quebrando os números em partes menores para reduzir o número de multiplicações. Ele segue os seguintes passos:
1. Se os números forem pequenos o suficiente, realiza a multiplicação diretamente.
2. Caso contrário, divide os números ao meio, separando as partes de ordem mais alta e mais baixa.
3. Faz três chamadas recursivas para multiplicar essas partes menores.
4. Usa as multiplicações obtidas para calcular o resultado final, reduzindo o número total de operações comparado ao método tradicional.

Esse processo reduz a complexidade da multiplicação de \( O(n^2) \) para aproximadamente \( O(n^{1.585}) \), tornando-o mais eficiente para números grandes.


```python
def karatsuba(x: int, y: int) -> int:
 if x < 10 or y < 10:
     return x * y
 else:
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    a = x // (10 ** (half)) # A = parte a esquerda de x
    b= x % (10 ** (half)) # B = parte a direita de x
    c = y // (10 ** (half)) # C = parte a esquerda de y
    d = y % (10 ** (half)) # D = parte a direita de y
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd   
```


## Como executar o projeto
Para executar o projeto, siga os passos abaixo:

### **Requisitos**
- Python 3 instalado.

### **Passos para execução**
1. Clone o repositório:
   ```bash
   git clone https://github.com/RenatoMAP77/Karatsuba.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd src
   ```
3. Execute o script principal:
   ```bash
   python app.py
   ```
4. Insira dois números inteiros para multiplicação e veja o resultado exibido no terminal.


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

#### Cálculo da Complexidade Ciclomática

Com isto explicado podemos partir para o calculo da complexidade ciclomática do algoritmo de Karatsuba. Para isso, vamos considerar o código do algoritmo como um grafo de controle de fluxo, onde os nós são os blocos de código e as arestas são as transições entre eles.

**N - Nós:**
1. Inicio da função
2. Verificação do `if`
3. Execução dentro do If (Retorno da multiplicação)
4. Cálculo do tamanho `n`
5. Cálculo de `half`
6. Cálculo das partes de `x` (`a` e `b`)
7. Cálculo das partes de `y` (`c` e `d`)
8. Chamada recursiva `karatsuba(a, c)`
9. Atribuição de `ac`
10. Chamada recursiva `karatsuba(b, d)`
11. Atribuição de `bd`
10. Chamada recursiva `karatsuba(a + b, c + d)`
11. Cálculo de `ad_plus_bc`
12. Retorno da multiplicação combinada

**E - Arestas:**
1. Início da função → Verificação do `if`
2. `if` verdadeiro → Retorno direto da multiplicação
3. `if` falso → Cálculo do tamanho `n`
4. Cálculo do tamanho `n` → Cálculo de `half`
5. Cálculo de `half` → Cálculo das partes de `x`
6. Cálculo das partes de `x` → Cálculo das partes de `y`
7. Cálculo das partes de `y` → Chamada `karatsuba(a, c)`
8. Chamada `karatsuba(a, c)` → Atibuição de `ac`
9. Atribuição de ac → Chamada `karatsuba(b, d)`
10. Chamada `karatsuba(b, d)` → Atribuição de `bd`
11. Atribuição de `bd` → Chamada `karatsuba(a + b, c + d)`
12. Chamada `karatsuba(a + b, c + d)` → Cálculo de `ad_plus_bc`
13. Cálculo de `ad_plus_bc` → Retorno da multiplicação combinada


Podendo ser melhor representado pela imagem a seguir do grafo de fluxo.

![Grafo de Fluxo](Diagrama_karatsuba.jpg)

**Aplicando a Fórmula:**

Usando a fórmula da complexidade ciclomática:
\(
M = E - N + 2P
\)
Onde:
- \( E = 13 \) (arestas)
- \( N = 12 \) (nós)
- \( P = 1 \) (um único componente conectado)

\(
M = 13 - 12 + 2(1) = 3
\)

### Análise de Complexidade Assintótica

 **Análise da complexidade temporal**

O algoritmo de Karatsuba melhora a eficiência da multiplicação tradicional reduzindo o número de operações necessárias. Em vez de realizar \( O(n^2) \) multiplicações como no método convencional, ele usa um esquema de divisão e conquista para reduzir essa complexidade. A cada nível da recursão, os números são divididos ao meio e três multiplicações menores são realizadas, além de operações adicionais de soma e potência de 10. Isso resulta em uma complexidade de tempo de aproximadamente:

\
O(n^{1.585})


Esse valor surge porque a cada passo reduzimos o tamanho do problema pela metade, mas realizamos três chamadas recursivas em vez de quatro, como aconteceria na multiplicação tradicional.

**Casos de Complexidade**
- **Melhor caso:** Ocorre quando os números são pequenos o suficiente para serem multiplicados diretamente, resultando em  O(1) .
- **Caso médio e pior caso:** Mantêm a complexidade  O(n^{1.585}), pois o algoritmo sempre segue a mesma estrutura recursiva.

---


#### Analise de Complexidade de Espaço



A complexidade espacial do algoritmo de Karatsuba depende da profundidade da recursão.

- Em cada chamada, o algoritmo faz 3 chamadas recursivas.

- A profundidade da recursão é O(log n) (pois a cada passo os números são reduzidos pela metade).

 Levando isto em consideração, a complexidade espacial do algoritmo de Karatsuba não foge de O(log n).

## Referências
https://www.youtube.com/watch?v=yWI2K4jOjFQ

https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/blob/main/PDF/AULA%2001_Análise%20de%20complexidade%20de%20algoritmos.pdf

https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/blob/main/PDF/AULA%2002_Introdução%20à%20teoria%20da%20complexidade.pdf