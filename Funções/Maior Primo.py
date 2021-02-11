def maior_primo(numero_inicial):
  numero_checagem = 1

  while numero_checagem <= numero_inicial:
    indice = 1
    cont = 0
    while indice <= numero_checagem:
      if numero_checagem % indice == 0:
        cont += 1

      indice += 1

    if cont == 2:
      maior = numero_checagem

    numero_checagem += 1

  return maior

a = int(input("Digite um número para verificação: "))
print("\nO maior número primo verificado é:", maior_primo(a))
