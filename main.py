# Inicialização dos contadores
excelente = 0
ruim = 0

# O enunciado pede 50, mas sugere testar com 10 primeiro.
# Altere o valor de 'range' conforme necessário.
total_entrevistados = 50 

print("--- Pesquisa de Satisfação TudoWeb ---")

for i in range(total_entrevistados):
    print(f"\nEntrevistado nº {i + 1}")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Qual sua opinião sobre o atendimento?")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = input("Sua resposta: ")

    # Estrutura de decisão para verificar a opinião
    if opiniao == "1":
        excelente += 1
    elif opiniao == "3":
        ruim += 1
    # Note que a opção 2 (BOM) não precisa de contador conforme o enunciado

print("\n--- Resultado Final da Pesquisa ---")
print(f"Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"Quantidade de respostas 'RUIM': {ruim}")
