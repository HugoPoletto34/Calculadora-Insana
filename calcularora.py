# Solicitar dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitar a operação desejada ao usuário
operacao = input("Escolha a operação (+, -, *, /): ")

# Realizar a operação escolhida e exibir o resultado
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        resultado = "Erro: divisão por zero"
    else:
        resultado = num1 / num2
else:
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")
