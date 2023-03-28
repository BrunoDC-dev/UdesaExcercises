cantPeces =  int(input("Ingrese y0: "))
pescaDiaria =  int(input("Ingrese X: "))
tasaRepro =  float(input("Ingrese alfa: "))
capacidadLago =  int(input("Ingrese beta: "))
proporcionDepredadores =  float(input("Ingrese gama: "))
cantDias =  int(input("Ingrese N: "))

def poblacionDiaria (cantPecesXdia):
    resultado  = cantPecesXdia+tasaRepro*cantPecesXdia*(capacidadLago-cantPecesXdia)-proporcionDepredadores*cantPecesXdia-pescaDiaria
    if resultado <0:
        return 0 
    return resultado

def calcularPoblacion (cantPeces):
    if cantPeces >50000:
        print("Valor Y0 no puede ser mayor a la cantidad maxima permitida")
        return
    if cantPeces <0 :
        print("Valor Y0 no puede ser negativa")
        return
    if tasaRepro <0:
        print("La tasa de reproduccion no puede ser menor a 0 ")
        return
    if proporcionDepredadores <0:
        print("La proporcion de peces comidos no puede ser menor a 0 ")
        return
    if pescaDiaria <0:
        print("La cantidad de pesa diaria no puede ser menor a 0")
        return
    print("""Tabla de valores:
t_i| y_i
-------------
0  |  """+str(cantPeces))
    for dia in range(cantDias):
        poblacion = poblacionDiaria(cantPeces)
        print(" "+ str(dia+1) + " | " +str(int(poblacion)))
        cantPeces= poblacion 
    return     

calcularPoblacion( cantPeces)