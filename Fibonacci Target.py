def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verifica_pertence(n, fib_sequence):
    if n in fib_sequence:
        return True
    else:
        return False

while True:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    sequencia_fibonacci = fibonacci_sequence(numero)
    if verifica_pertence(numero, sequencia_fibonacci):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
    repetir = input("Deseja verificar outro número? (S/N): ")
    while repetir.upper() not in ['S', 'N']:
        repetir = input("Resposta inválida. Por favor, responda com 'S' para Sim ou 'N' para Não: ")
    
    if repetir.upper() != 'S':
        break
