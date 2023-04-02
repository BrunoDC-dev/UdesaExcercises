cantPeces = 24487 
TasaRepro = 0.000082  
CapacidadLago = 24487  
DepreProporciones = 0.1  
pescaDiaria = 237  
cantDias = 90  
    # función que calcula la población de peces en un día determinado
def poblacionDiaria(cantPecesXdia, pescaDiariaFuncion):
        resultado = cantPecesXdia + TasaRepro * cantPecesXdia * (CapacidadLago - cantPecesXdia) - DepreProporciones * cantPecesXdia - pescaDiariaFuncion
        if resultado < 0:
            return 0
        elif resultado > 50000:
            return 50000 
        return resultado 

    # función  calcula la población de peces en el lago después de un periodo determinado de días
def poblacion90Dias(cantPeces, pescaDiariaFuncion):
        pecesFor = cantPeces
        for dia in range(cantDias):
            poblacion = poblacionDiaria(pecesFor, pescaDiariaFuncion)
            pecesFor = poblacion
            if pecesFor == 0:
                break 
        return poblacion

    # funcion busca la población minima posible que puede mantenerse durante un periodo determinado de días sin llegar a cero
def calcularPoblacion(cantPecesFuncion, pescaDiariaFuncion):
        while True:    
            resultado = poblacion90Dias(cantPecesFuncion, pescaDiariaFuncion)
            if resultado > 0:
                maximoPoblacion = int(cantPecesFuncion)
                cantPecesFuncion -= 1
            else:
                break
        print("Una poblacion de " + str(maximoPoblacion ))

calcularPoblacion(cantPeces, pescaDiaria) 
