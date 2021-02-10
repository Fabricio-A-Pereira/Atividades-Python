num = int(input("Digite um número: "))
num_inicial = num
fat = 1

while num > 1:
  fat = fat * num
  num = num - 1

print("O fatorial de", num_inicial, "é:", fat)
