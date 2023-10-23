#exercicio 01

def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def main():
    try:
        n = int(input("Informe um valor inteiro (n): "))
        imprimir_padrao(n)
    except ValueError:
        print("Por favor, insira um valor inteiro válido para n.")

if __name__ == "__main__":
    main()





#exercicio 02

def contar_digitos(numero):
    # Converte o número para uma string e calcula o comprimento da string
    numero_str = str(numero)
    quantidade_digitos = len(numero_str)
    return quantidade_digitos

def main():
    try:
        numero = int(input("Informe um número inteiro: "))
        quantidade = contar_digitos(numero)
        print(f"O número {numero} tem {quantidade} dígitos.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()

    
    
    
    
    
    #exercicio 03

    def calcular_divisao():
     try:
        numero1 = int(input("Informe o primeiro número inteiro: "))
        numero2 = int(input("Informe o segundo número inteiro: "))
        resultado = numero1 / numero2
     except ValueError:
        print("Erro: Certifique-se de inserir números inteiros válidos.")
     except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
     else:
        print(f"A divisão de {numero1} por {numero2} é igual a {resultado:.2f}")
     finally:
        print("Fim da operação.")

def main():
    calcular_divisao()

if __name__ == "__main__":
    main()





