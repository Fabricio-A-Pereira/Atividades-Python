a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if (a < b and a < c) and (b < c):
  print("\nEstão em ordem crescente!")
else:
  print("\nNão estão em ordem crescente.")
