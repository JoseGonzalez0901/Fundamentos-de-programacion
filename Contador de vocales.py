nombre=input("¿Cómo te llamas? ")
vocales=['a','e','i','o','u']
i=0
while True:
  for vocal in nombre:
    if vocal in vocales:
      i=i+1

  if i>=3:
    print("Tu nombre tiene",i,"vocales","y te llamas:",nombre)
    break
  else:
    print("Intentalo de nuevo")
    nombre=input("¿Cómo te llamas? ")
    i=0


