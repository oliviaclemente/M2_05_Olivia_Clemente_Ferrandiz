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
contador=0
while True:
  letra= input("Introduce una palabra:")
  if letra=="a":
      contador+=1
  elif letra== ".":
      break
print("Entonces la letra 'a' se ha introducido {contador} veces")
print("")
#ejercicio 4
CP= "Introduce palabra:"
CP+= "Introduce palabra:"
listaP = CP.split()
input("La cadena de palabra es:")
print(listaP)
input("La longitud es:")
print(len(listaP))

long= []
for i in range(0, (len(listaP[1]))):
  long.append(len(listaP[1][i]))
print(long)