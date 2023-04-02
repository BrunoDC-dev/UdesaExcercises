cantPeces = 24487*0.9 
TasaRepro = 0.000082 
CapacidadLago = 24487 
DepreProporciones = 0.1 
pescaDiaria = 0 
cantDias = 90 

def poblacionDiaria(cantPecesXdia, pescaDiariaFuncion):
    # función que calcula la población diaria de peces
    resultado = cantPecesXdia + TasaRepro * cantPecesXdia * (CapacidadLago - cantPecesXdia) - DepreProporciones * cantPecesXdia - pescaDiariaFuncion
    if resultado < 0:
        return 0 
    elif resultado > 50000:
        return 50000
    return resultado


def poblacion90Dias(cantPeces, pescaDiariaFuncion):
    # función que calcula la población de peces durante 90 días
    for dia in range(cantDias):
        poblacion = poblacionDiaria(cantPeces, pescaDiariaFuncion)
        cantPeces = poblacion 
        if cantPeces == 0:
            break
    return poblacion


def calcularPoblacion(cantPeces, pescaDiariaFuncion):
    # función que encuentra el máximo de pesca diaria permitido sin reducir la población de peces por debajo de cero
    while True:    
        resultado = poblacion90Dias(cantPeces, pescaDiariaFuncion)
        if resultado > 0:
            maximoPesca = pescaDiariaFuncion
            maximoPoblacion = int(resultado)
            pescaDiariaFuncion += 1
        else:
            break    
    print("Un Maximo de Pesca de " + str(maximoPesca) + " con una poblacion de " + str(maximoPoblacion))


calcularPoblacion(cantPeces, pescaDiaria)
