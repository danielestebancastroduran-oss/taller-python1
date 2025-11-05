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
#Hacer un algoritmo que permita determinar la cantidad de minutos a los que equivale una cantidad de horas ingresadas por el usuario.
print("conversion de horas a minutos")
horas = input("ingrese la cantidad de horas a convertir: ")
minutos = float(horas) * 60
print("la cantidad de horas ingresadas equivalen a: ", minutos, "minutos")
print("fin del programa")
#Desarrollar un algoritmo que permita convertir de quintal a kilogramos, tenga en cuenta que un quintal equivale a 100 kilogramos.
print("conversion de quintales a kilogramos")
quintales = input("ingrese la cantidad de quintales a convertir: ") 
kilogramos = float(quintales) * 100
print("la cantidad de quintales ingresados equivalen a: ", kilogramos, "kilogramos")
print("fin del programa")
#el costo de 4 llamadas telefonicas
print("costo de llamadas telefonicas")
costo1 = input("ingrese el costo de la primera llamada al primer operador: ")
costo2 = input("ingrese el costo de la segunda llamada al primer operador: ")
costo3 = input("ingrese el costo de la primera llamada al segundo operador: ")
costo4 = input("ingrese el costo de la segunda llamada al segundo operador: ")
totaloperador1 = float(costo1) + float(costo2)
totaloperador2 = float(costo3) + float(costo4)
totalgeneral = totaloperador1 + totaloperador2
print("el costo total de las llamadas al primer operador es: ", totaloperador1)
print("el costo total de las llamadas al segundo operador es: ", totaloperador2)
print("el costo total de las cuatro llamadas es: ", totalgeneral)
print("fin del programa")
#enchapar muros de baño
print("calculo de baldosas necesarias para enchapar un baño")
alto = input("ingrese el alto del muro en metros: ")
ancho = input("ingrese el ancho del muro en metros: ")
area = float(alto) * float(ancho)
baldosasnecesarias = area / 3.5
print("el area del muro es: ", area, "metros cuadrados")
print("la cantidad de baldosas necesarias para enchapar el muro es: ", baldosasnecesarias, "cajas")
print("fin del programa")
#atleta quieree saber cuanto tiempo recorrio.
print("datos del entrenamiento del atleta")
tiempo1 = input("ingrese el tiempo del primer día de entrenamiento en minutos: ")
tiempo2 = input("ingrese el tiempo del segundo día de entrenamiento en minutos: ")
tiempo3 = input("ingrese el tiempo del tercer día de entrenamiento en minutos: ")
distancia1 = input("ingrese la distancia del primer día de entrenamiento en metros: ")
distancia2 = input("ingrese la distancia del segundo día de entrenamiento en metros: ")
distancia3 = input("ingrese la distancia del tercer día de entrenamiento en metros: ")
tiempototal = float(tiempo1) + float(tiempo2) + float(tiempo3)
distanciatotal = float(distancia1) + float(distancia2) + float(distancia3)
tiempopromedio = tiempototal / 3    
distanciapromedio = distanciatotal / 3
print("el tiempo total de entrenamiento es: ", tiempototal, "minutos")
print("la distancia total recorrida es: ", distanciatotal, "metros")
print("el tiempo promedio de entrenamiento es: ", tiempopromedio, "minutos")
print("la distancia promedio recorrida es: ", distanciapromedio, "metros")
print("fin del programa")
#herencia madre e hijos
print("datos de la herencia")
herencia = input("ingrese el valor total de la herencia: ")
madre = float(herencia) * 0.5
hijo = (float(herencia) * 0.5) / 4
print("la madre recibira: ", madre)
print("cada hijo recibira: ", hijo)
print("fin del programa")
#herecia a esposa e hijos segun testamento
print("datos de la herencia segun testamento")
herencia = input("ingrese el valor total de la herencia: ")
esposa = float(herencia) * 0.4
hijo1 = float(herencia) * 0.3
hijo2 = float(herencia) * 0.2
hijo3 = float(herencia) * 0.4
hijo4 = float(herencia) * 0.1
print("la esposa recibira: ", esposa)
print("el primer hijo recibira: ", hijo1)
print("el segundo hijo recibira: ", hijo2)
print("el tercer hijo recibira: ", hijo3)
print("el cuarto hijo recibira: ", hijo4)
print("fin del programa")
#El terreno comprado por un influencers para proyectos
print("destinacion del terreno comprado por un influencer")
areatotal = input("ingrese el area total del terreno en metros cuadrados: ")
cultivos = float(areatotal) * 0.4
vivienda = float(areatotal) * 0.25
zonasverdes = float(areatotal) * 0.15
otrosproyectos = float(areatotal) - (cultivos + vivienda + zonasverdes)
print("el area destinada para cultivos es: ", cultivos, "metros cuadrados")
print("el area destinada para construir vivienda es: ", vivienda, "metros cuadrados")
print("el area destinada para zonas verdes es: ", zonasverdes, "metros cuadrados")
print("el area disponible para otros proyectos es: ", otrosproyectos, "metros cuadrados")
print("fin del programa")
#caliificacion de calze de programacion talleres quizz
print("calculo de la nota definitiva de un estudiante")
taller1 = input("ingrese la nota del primer taller: ")
taller2 = input("ingrese la nota del segundo taller: ")
promediotalleres = (float(taller1) + float(taller2)) / 2
evaluacion1 = input("ingrese la nota de la primera evaluacion: ")
evaluacion2 = input("ingrese la nota de la segunda evaluacion: ")
evaluacion3 = input("ingrese la nota de la tercera evaluacion: ")
promedioevaluaciones = (float(evaluacion1) + float(evaluacion2) + float(evaluacion3)) / 3
trabajofinal = input("ingrese la nota del trabajo final: ")
quiz1 = input("ingrese la nota del primer quiz: ")
quiz2 = input("ingrese la nota del segundo quiz: ")
quiz3 = input("ingrese la nota del tercer quiz: ")
quiz4 = input("ingrese la nota del cuarto quiz: ")
promedioquizzes = (float(quiz1) + float(quiz2) + float(quiz3) + float(quiz4)) / 4
notadefinitiva = (promediotalleres * 0.15) + (promedioevaluaciones * 0.30) + (float(trabajofinal) * 0.30) + (promedioquizzes * 0.25)
print("la nota definitiva del estudiante es: ", notadefinitiva)
print("fin del programa")
#liquidacion de conductor de bus
print("liquidacion de conductor de bus")
numeroinicial = input("ingrese el numero inicial de la registradora: ")
numerofinal = input("ingrese el numero final de la registradora: ")
valorpasaje = input("ingrese el valor del pasaje: ")
totalpasajeros = float(numerofinal) - float(numeroinicial)
valortotal = totalpasajeros * float(valorpasaje)
valorconductor = valortotal * 0.25
valorempresa = valortotal * 0.75
print("el total de pasajeros transportados es: ", totalpasajeros)
print("el valor liquidado al conductor es: ", valorconductor)
print("el valor liquidado a la empresa es: ", valorempresa)
print("fin del programa")
