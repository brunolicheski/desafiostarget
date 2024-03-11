def inverte_string(string):
    inverted_string = ''
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

while True:
    string_original = input("Digite uma string para inverter: ")

    string_invertida = inverte_string(string_original)
    print("String original:", string_original)
    print("String invertida:", string_invertida)
    
    repetir = input("Deseja inverter outra string? (S/N): ")
    while repetir.upper() not in ['S', 'N']:
        repetir = input("Resposta inválida. Por favor, responda com 'S' para Sim ou 'N' para Não: ")
    
    if repetir.upper() != 'S':
        break
