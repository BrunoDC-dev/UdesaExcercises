# función para pedir un valor numérico al usuario y manejar posibles errores
def pedirNumero(mensaje, tipo):
    while True:
        valor = input(mensaje)
        try:
            valor = tipo(valor)
            return valor
        except ValueError:
            if tipo==int:
                print("Error: el valor ingresado debe ser un número entero.")
            else:
                print("Error: el valor ingresado debe ser un número")

# función para calcular la población en un día determinado basándose en la población actual
def poblacionDiaria(cantPecesXdia, tasaRepro, capacidadLago, proporcionDepredadores, pescaDiaria):
    resultado = cantPecesXdia + tasaRepro * cantPecesXdia * (capacidadLago - cantPecesXdia) - proporcionDepredadores * cantPecesXdia - pescaDiaria
    # Asegurarse de que la población no sea inferior a 0 ni superior a la población máxima permitida
    if resultado < 0:
        return 0 
    elif resultado > 50000:
        return 50000
    return resultado

# función para calcular la población a lo largo de varios días
def calcularPoblacion():
    # Pedir los valores de entrada al usuario y manejar posibles errores
    
    cantPeces = pedirNumero ("Ingrese y0: ", int)
    while cantPeces > 50000 or cantPeces < 0:
        print("Error: la cantidad de peces no puede ser mayor a 50000 ni menor a 0.")
        cantPeces = pedirNumero ("Ingrese y0: " , int)
    
    pescaDiaria = pedirNumero ("Ingrese X: " ,float)
    while pescaDiaria < 0:
        print("Error: la cantidad de pesca diaria no puede ser menor a 0.")
        pescaDiaria = pedirNumero ("Ingrese X: ", float)
        
    tasaRepro = pedirNumero("Ingrese alfa: ", float)
    while tasaRepro < 0:
        print("Error: la tasa de reproducción no puede ser menor a 0.")
        tasaRepro = pedirNumero("Ingrese alfa: ", float)
    
    capacidadLago = pedirNumero ("Ingrese beta: ", int)
    while capacidadLago > 50000 or capacidadLago < 0:
        print("Error: la capacidad del lago no puede ser mayor a 50000 ni menor a 0.")
        capacidadLago = pedirNumero ("Ingrese Beta: " , int)
    
    proporcionDepredadores = pedirNumero("Ingrese gama: " , float)
    while proporcionDepredadores < 0:
        print("Error: la proporción de peces comidos por depredadores no puede ser menor a 0.")
        proporcionDepredadores = pedirNumero("Ingrese gama: ", float)
    
    cantDias = pedirNumero ("Ingrese N: " , int)
    while  cantDias < 0:
        print("Error: La cantida de dias no puede ser menor a 0")
        cantDias = pedirNumero ("Ingrese N: ", int)

    print("""Tabla de valores:
t_i | y_i
-------------
0  |  """ + str(cantPeces))

    # Iterar sobre el número especificado de días y calcular la población para cada día
    for dia in range(cantDias):
        poblacion = poblacionDiaria(cantPeces, tasaRepro, capacidadLago, proporcionDepredadores, pescaDiaria)
        print(" " + str(dia + 1) + " | " + str(int(poblacion)))
        cantPeces = poblacion

    return

calcularPoblacion()
