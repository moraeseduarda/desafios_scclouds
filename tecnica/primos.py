import math
n = int(input())

def primos_linear(n):
  primos = []
  if n <= 1:
    return primos
  primos.append(2)
  for i in range(3, n+1, 2):
    # começa em 3, n+1, pula de 2 em dois pra pegar ímpares
    raiz = int(math.sqrt(i)) 
    eh_primo = True
    for j in range(3, raiz+1, 2): # do três até a raiz de n
      if i % j == 0:
        eh_primo = False
        break
    if eh_primo:
      primos.append(i)
  return primos

resultado_linear = primos_linear(n)
print(resultado_linear)

def eh_primo(n, divisor=None):
    if divisor is None:
      divisor = n - 1
    # Essa é a condição para ser primo, possuir apenas um divisor, ele mesmo
    # Por isso o 2 entra na lista, só divide a si mesmo
    if divisor == 1:
        return True
    if n % divisor == 0:
      return False
    return eh_primo(n, divisor - 1)

def primos_recursiva(n):
  primos = []
  if n <= 1:
    return primos
  primos_anteriores = primos_recursiva(n - 1)
  if eh_primo(n):
    primos_anteriores.append(n)
  return primos_anteriores
  
resultado_recursivo = primos_recursiva(n)
print(resultado_recursivo)