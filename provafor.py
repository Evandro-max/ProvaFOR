numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro, maior que o primeiro: "))
soma = 0

for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        soma += i

if soma > 0:
    print(f"Soma dos números pares entre os números = {soma}")
else:
    print("Não existe números pares no intervalo.")