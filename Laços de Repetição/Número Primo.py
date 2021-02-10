num = int(input("Digite um número inteiro: "))
i = 1
cont = 0

while i <= num:
  if num % i == 0:
    cont += 1

  i += 1

if cont == 2:
  print("Primo")
else:
  print("Não primo")
