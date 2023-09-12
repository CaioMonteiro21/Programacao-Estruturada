def calcular_parcelas(divida, parcelas):
    if parcelas == 1:
        juros = 0.0
    elif parcelas == 3:
        juros = 10.0
    elif parcelas == 6:
        juros = 15.0
    elif parcelas == 9:
        juros = 20.0
    elif parcelas == 12:
        juros = 25.0
    else:
        print("Número de parcelas inválido.")
        return
    
    valor_juros = (divida * juros) / 100
    valor_total = divida + valor_juros
    valor_parcela = valor_total / parcelas
    
    print("\nOpção de pagamento:")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor dos juros: {valor_juros}")
    print(f"Valor total da dívida: {valor_total}")
    print(f"Valor da parcela: {valor_parcela}")

def main():
    divida = float(input("Digite o valor da dívida: "))
    
    print("\nOpções de parcelamento:")
    print("1 - 0% de juros")
    print("3 - 10% de juros")
    print("6 - 15% de juros")
    print("9 - 20% de juros")
    print("12 - 25% de juros")
    
    parcelas = int(input("Escolha o número de parcelas (1, 3, 6, 9 ou 12): "))
    
    calcular_parcelas(divida, parcelas)

if __name__ == "__main__":
    main()




# Inicialize as contagens para cada intervalo

intervalo_1_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break  # Sai do loop se for inserido um número negativo
    
    if 0 <= numero <= 25:
        intervalo_1_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

# Exibe os resultados
print(f"Números no intervalo [0-25]: {intervalo_1_25}")
print(f"Números no intervalo [26-50]: {intervalo_26_50}")
print(f"Números no intervalo [51-75]: {intervalo_51_75}")
print(f"Números no intervalo [76-100]: {intervalo_76_100}")