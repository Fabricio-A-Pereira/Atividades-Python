import math # importando a biblioteca

# Funções
def fun_delta(a, b, c):
  delta = (b ** 2) - 4 * a * c
  return delta

def raizes_x1(a, b, delta):
  if delta >= 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    return x1
  else:
    x1 = 0
    return x1

def raizes_x2(a, b, delta):
  if delta > 0:
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    return x2
  else:
    x2 = 0
    return x2

def imprime(a, b, c, delta, x1, x2):
  if delta > 0:
    print("\nResultado...")
    print("A:", a, "\nB:", b, "\nC:", c)
    print("Delta:", delta)
    print("Raíz 1:", x1, "\nRaíz 2:", x2)
  elif delta == 0:
    print("\n- Resultado...")
    print("A:", a, "\nB:", b, "\nC:", c)
    print("Delta:", delta)
    print("Raíz 1:", x1)
    print("\nNa equação onde o delta é igual à 0, as raízes são iguais ou existe apenas uma.")
  else:
    print("\nCom o delta negativo, não tem como realizar a operação.")

# Função Principal
def main():
  a = int(input("Digite o valor de A: "))
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))

  delta = fun_delta(a, b, c)
  x1 = raizes_x1(a, b, delta)
  x2 = raizes_x2(a, b, delta)

  imprime(a, b, c, delta, x1, x2)


# Executando...
main()
