cantPeces = 24487*0.9
TasaRepro= 0.000082
CapacidadLago=24487
DepreProporciones= 0.1
pescaDiaria=0
cantDias=90
def poblacionDiaria (cantPecesXdia, pescaDiariaFuncion):
    resultado  = cantPecesXdia+TasaRepro*cantPecesXdia*(CapacidadLago-cantPecesXdia)-DepreProporciones*cantPecesXdia-pescaDiariaFuncion
    if resultado <0:
        return 0 
    return resultado


def poblacion90Dias(cantPeces,pescaDiariaFuncion):
    for dia in range(cantDias):
            poblacion = poblacionDiaria(cantPeces,pescaDiariaFuncion)
            cantPeces= poblacion 
            if cantPeces == 0:
                break
    return poblacion

def calcularPoblacion (cantPeces,pescaDiariaFuncion):
    while True :    
        resultado = poblacion90Dias( cantPeces,pescaDiariaFuncion)
        if resultado >0 :
            maximoPesca= pescaDiariaFuncion
            maximoPoblacion= int(resultado)
            pescaDiariaFuncion +=1
        else:
            break    
    print("Un Maximo de Pesca de " +  str( maximoPesca) + " con una poblacion de " + str(maximoPoblacion ))
calcularPoblacion( cantPeces,pescaDiaria)