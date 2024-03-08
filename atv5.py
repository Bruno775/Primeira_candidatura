def inverter_string(s): #função a ser utilizada 
    # Usando slicing para inverter a string
    return s[::-1]

# Solicita ao usuário uma string
string_original = input("Digite uma string: ")

# Chama a função para inverter a string
string_invertida = inverter_string(string_original)

# Exibe a string invertida
print(f"A string invertida é: {string_invertida}")