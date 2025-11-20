import random

def calcular_crecimiento(luz, agua, nutrientes):
    crecimiento_base = (0.5 * luz + 0.3 * agua + 0.2 * nutrientes)

    if crecimiento_base < 0:
        crecimiento_base = 0
    if crecimiento_base > 1:
        crecimiento_base = 1

    return crecimiento_base

def regar(agua):
    agua += random.uniform(0.2, 0.5)
    if agua > 1:
        agua = 1
    return agua

def medir_estres(agua):
    if agua < 0.3:
        return "Falta de agua (estrés)"
    elif agua > 0.8:
        return "Exceso de agua (estrés)"
    else:
        return "Agua en nivel ideal"

def crecer(tamano, crecimiento):
    return tamano + crecimiento * 0.5  

print("SIMULADOR DE CRECIMIENTO DE UNA PLANTA")

tamano = 1.0           
agua = 0.5             
nutrientes = 0.6      
dias = int(input("¿Cuántos días deseas simular? "))

print("Día | Tamaño | Agua | Crecimiento | Estado del Agua")
print("-----------------------------------------------------")

for dia in range(1, dias + 1):

    luz = random.uniform(0.3, 1.0)

    if random.random() < 0.4:  
        agua = regar(agua)

    estado_agua = medir_estres(agua)

    crecimiento = calcular_crecimiento(luz, agua, nutrientes)

    tamano = crecer(tamano, crecimiento)

    agua -= 0.1
    if agua < 0:
        agua = 0

    print(f"{dia:3d} | {tamano:6.2f} | {agua:4.2f} | {crecimiento:10.2f} | {estado_agua}")

print("La simulación ha terminado.")
