operacao = str(input("Qual a operação que você deseja fazer na calculadora?\n1 = + (adição)\n2 = - (subtração)\n3 = * (multiplicação)\n4 = / (divisão)\n"))

while operacao != '1' and operacao != '2' and operacao != '3' and operacao != '4':
  operacao = str(input("Digite 1, 2, 3 ou 4...\n"))

if operacao == '1':
  valor = float(input("Digite o primeiro valor a ser somado: "))
  valor2 = float(input("Digite o segundo valor a ser somado: "))
  valorFinal = valor + valor2
  print(f"O valor final da soma de {valor} e {valor2} é {valorFinal}")
elif operacao == '2':
  valor = float(input("Digite o primeiro valor a ser subtraído: "))
  valor2 = float(input("Digite o segundo valor a ser subtraído: "))
  valorFinal = valor - valor2
  print(f"O valor final da subtração de {valor} e {valor2} é {valorFinal}")
elif operacao == '3':
  valor = float(input("Digite o primeiro valor a ser multiplicado: "))
  valor2 = float(input("Digite o segundo valor a ser multiplicado: "))
  valorFinal = valor * valor2
  print(f"O valor final da multiplicação de {valor} e {valor2} é {valorFinal}")
elif operacao == '4':
  valor = float(input("Digite o primeiro valor a ser dividido: "))
  valor2 = float(input("Digite o segundo valor a ser dividido: "))
  valorFinal = valor / valor2
  print(f"O valor final da divisão de {valor} e {valor2} é {valorFinal}")