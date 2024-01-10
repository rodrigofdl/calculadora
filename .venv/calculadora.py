import math

print("\n******************* Calculadora(simples) em Python *******************")

ad = lambda num1, num2: num1 + num2
sub = lambda num1, num2: num1 - num2
mul = lambda num1, num2: num1 * num2
div = lambda num1, num2: num1 / num2
res = lambda num1, num2: num1 % num2
expo = lambda num1, num2: num1 ** num2
sqrt = lambda num1: math.sqrt(num1)

ope = input(
    "\nQual operação a ser realizada (adição, subtração, multiplicação, divisão, resto, exponenciação, raiz quadrada)? ")


if ope == 'adição'.lower():
    num1 = float(input("Digite a primeira parcela: "))
    num2 = float(input("Digite a segunda parcela: "))
    print("Soma: ", ad(num1, num2))
elif ope == 'subtração'.lower():
    num1 = float(input("Digite o minuendo: "))
    num2 = float(input("Digite o subtraendo: "))
    print("Diferença: ", sub(num1, num2))
elif ope == 'multiplicação'.lower():
    num1 = float(input("Digite o primeiro fator: "))
    num2 = float(input("Digite o segundo fator: "))
    print("Produto: ", mul(num1, num2))
elif ope == 'divisão'.lower():
    num1 = float(input("Digite o dividendo: "))
    num2 = float(input("Digite o divisor: "))
    print("Quociente", div(num1, num2))
elif ope == 'resto'.lower():
    num1 = float(input("Digite o dividendo: "))
    num2 = float(input("Digite o divisor: "))
    print("Resto: ", res(num1, num2))
elif ope == 'exponenciação'.lower():
    num1 = float(input("Digite a base: "))
    num2 = float(input("Digite o expoente: "))
    print("Potência: ", expo(num1, num2))
elif ope == 'raiz quadrada'.lower():
    num1 = float(input("Digite o radicando: "))
    print("Raiz quadrada: ", sqrt(num1))
else:
    print("Opção inválida!\nExecute o código novamente.")
