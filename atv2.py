#Será a toma dos 2 valores anteriores

def fibonacci_sequence(n):
    # Inicializa os primeiros dois termos da sequência
    t1, t2 = 0, 1

    # Se n for 0 ou 1, já está na sequência
    if n == t1 or n == t2:
        return True

    # Calcula os próximos termos até atingir ou ultrapassar n
    while t2 <= n:
        next_term = t1 + t2
        if next_term == n:
            return True
        t1, t2 = t2, next_term

    # Se chegarmos aqui, o número não está na sequência
    return False

# Solicita ao usuário um número
try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Por favor, insira um número positivo.")
    else:
        if fibonacci_sequence(numero):
            print(f"{numero} pertence à sequência de Fibonacci.")
        else:
            print(f"{numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Entrada inválida. Certifique-se de inserir um número inteiro positivo.")

