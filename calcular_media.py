# Criador Douglas Magalhães de Vasconcelos
# calcular_media.py

def media(numb1, numb2, numb3):
    return (numb1+numb2+numb3)/3

notas = {}

while True:
    try:
        nome = input("Digite seu nome: ").title()
        numb1 = float(input("Digite a primeira nota: "))
        numb2 = float(input("Digite a segunda nota: "))
        numb3 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Entrada invalida1!")
        continue

    resultado = media(numb1,numb2,numb3)
    notas[nome] = resultado

    if resultado < 7.50:
        print(f"Você foi reprovado (média: 7.50): {resultado:.2f}")
    else:
        print(f"Você foi aprovado (média: 7.50): {resultado:.2f}")
    
    exibir = input("Deseja ver a nota de cada aluno? Digite (0) ou (1) para sair: ")

    if exibir == '0':
        for chave, value in notas.items():
            print(f"Alunos - {chave}: {value:.2f}")
    elif exibir == '1':
        print("Obrigado por usar nossa calculadora de média de notas de alunos!")
        break
    else:
        continue
