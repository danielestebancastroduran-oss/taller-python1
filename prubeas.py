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
