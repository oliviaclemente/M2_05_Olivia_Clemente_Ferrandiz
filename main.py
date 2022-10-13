#ejercicio 1
a = int(input("Introduce un número:"))
b = int(input("Introduce un número diferente:"))
c = int(input("Introduce otro número"))
if a == 0:
  print("No es correcto ya que es 0")
elif a < b < c:
  print("Se muestra en orden ascendente")
else:
  print("Se muestra en orden descendente")
print("")
#ejercicio 2
valores = []
print("Introduce 3 valores")
for x in range(3):
  valores.append(input("Intrduce un valor:"))
print(valores)
if valores == 0:
  print("No es correcto ya que es 0")
elif a<b<c:
  print("Se muestra en orden ascendente")
else:
  print("Se muestra en orden descendente")
print("")
#ejercicio 3
letra = []
print("Introduce 3 letras:")
for x in range(3):
  letra.append(input("Introduce una letra:"))
print(letra)
