#salario de bonifcacion
print("datos personales")
nombre = input("ingrese su nombre: ")
salario = input("ingrese su salario: ")
salarioconbonificacion = (float(salario) + 1.5)
print("su nombre es: ", nombre) 
print("su salario con bonificacion es: ", salarioconbonificacion)
print("fin del programa")
#cancha de futbol ampliada 20%
print("datos de la cancha")
largo = input("ingrese el largo de la cancha en metros: ")
ancho = input("ingrese el ancho de la cancha en metros: ")
areainicial = float(largo) * float(ancho)
areafinal = areainicial + (areainicial * 0.2)
print("el area inicial de la cancha es: ", areainicial, "metros cuadrados")
print("el area final de la cancha con ampliacion es: ", areafinal, "metros cuadrados")
print("fin del programa")
#desempleo ibague
print("datos del desempleo")
desempleoinicial = input("ingrese el porcentaje inicial de desempleo: ")
desempleoprimertrimestre = (float(desempleoinicial) + (float(desempleoinicial) * 0.095))
desempleosegundotrimestre = (float(desempleoprimertrimestre) - (float(desempleoprimertrimestre) * 0.015))
print("el desempleo inicial es: ", desempleoinicial, "%")
print("el desempleo en el primer trimestre es: ", desempleoprimertrimestre, "%")
print("el desempleo en el segundo trimestre es: ", desempleosegundotrimestre, "%")
print("fin del programa")
#Calcular area terreno reducida
print("datos del terreno")
areareducida = input("ingrese el area reducida del terreno en metros cuadrados: ")
areainicial = float(areareducida) / 0.9
areafinal = areainicial + (areainicial * 0.5)
print("el area inicial del terreno es: ", areainicial, "metros cuadrados")
print("el area final del terreno es: ", areafinal, "metros cuadrados")
print("fin del programa")
#Hacer un algoritmo que permita determinar las horas a las que equivale una cantidad de minutos ingresados por el usuario.
print("conversion de minutos a horas")
minutos = input("ingrese la cantidad de minutos a convertir: ")
horas = float(minutos) / 60
print("la cantidad de minutos ingresados equivalen a: ", horas, "horas")
print("fin del programa")


