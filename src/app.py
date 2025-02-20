#App para o usuario inserir 2 numeros e rodar o algoritmo de karatsuba

from main import karatsuba
def main():
    num1 = input("Primeiro Número: ")
    num2 = input("Segundo Número: ")
    
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Por favor insira 2 inteiros válidos.")
        return
    
    result = karatsuba(num1, num2)
    print(f"O resultado da multiplicação pelo método de karatsuba é: {result}")

if __name__ == "__main__":
    main()