#ex-1
import random

num_lancamentos = 100

contadores = [0, 0, 0, 0, 0, 0]

for _ in range(num_lancamentos):
    resultado = random.randint(1, 6)  
    contadores[resultado - 1] += 1  


for i in range(6):
    print(f'Número {i + 1}: {contadores[i]} vezes')



#ex-2


    import json


dados_alunos = {}


while True:
    matricula = input("Informe a matrícula do aluno (ou deixe em branco para encerrar): ")
    if not matricula:
        break
    
    nome = input("Nome do aluno: ")
    email = input("E-mail do aluno: ")

    dados_alunos[matricula] = {
        "nome": nome,
        "e-mail": email
    }


with open("dados_alunos.json", "w") as arquivo:
    json.dump(dados_alunos, arquivo, indent=4)

print("Dados dos alunos foram salvos em 'dados_alunos.json'.")



#ex-3




from datetime import datetime

def formatar_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        data_formatada = data.strftime('%d de %B de %Y')
        return data_formatada
    except ValueError:
        return None


data_str = input("Digite uma data no formato DD/MM/AAAA: ")
data_formatada = formatar_data(data_str)

if data_formatada:
    print(f'Data formatada: {data_formatada}')
else:
    print('Data inválida. Por favor, insira uma data válida no formato DD/MM/AAAA.')

