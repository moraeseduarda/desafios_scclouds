import math

# n é o nésimo termo
# 0,1,1,2,3,5,8,13,21,...

n = int(input())

# Resolução da sequência de fibonacci de forma recursiva:
def fib_recursiva(n):
  if n == 0 or n == 1:
    return n
  else:
    return fib_recursiva(n-1) + fib_recursiva(n-2)


# Resolução da sequência de fibonacci de forma linear:
def fib_linear(n):
  resultado = 0
  anterior = 0
  atual = 1
  if n == 0 or n == 1:
    return n
  else:
    for i in range(1,n):
      resultado = anterior + atual
      anterior = atual
      atual = resultado
    return resultado

# Coloquei uma forma extra de resolver a sequência, usando fórmula (fórmula geral para os números de fibonacci usando razão áurea).
razao_aurea = 1.6180334
def fib_formula(n):
  """Usa fórmula para retornar o enésimo (n) termo da sequência de fibonacci, arredonda o valor para eliminar casas decimais provenientes do cálculo."""
  resultado = (1/math.sqrt(5)) * (razao_aurea**n - (-1/razao_aurea)**n)
  return round(resultado)

resultado_recursivo = fib_recursiva(n)
print(f"Resultado fibonacci recursivo: {resultado_recursivo}")

resultado_linear = fib_linear(n)
print(f"Resultado fibonacci linear: {resultado_linear}")

resultado_formula = fib_formula(n)
print(f"Resultado fibonacci com fórmula: {resultado_formula}")

