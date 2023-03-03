#%% LIBRERIAS
import random
import matplotlib.pyplot as plt

#%% 01 GENERAR BOSQUE
def generar_bosque (n, debug = False):
    bosque = [0] * n
    if debug:
        print (bosque)
    return bosque
# generar_bosque (10)

#%% SUCESO ALEATORIO
def suceso_aleatorio (p, debug = False):
    suceso = False
    prob = random.randint(0, 100)
    if prob <= p:
        suceso = True
    if debug:
        print(suceso)
    return suceso
# suceso_aleatorio(80)

#%% 02 BROTES
def brotes(bosque, p, debug = False):
    for i in range (len(bosque)):
        brote = suceso_aleatorio(p)
        if brote == True:
            bosque[i] = 1
    if debug:
        print (bosque)
    return bosque
# brotes(generar_bosque(10), 80)

#%% 03 CUENTA QUE HAY EN CADA ESPACIO
def cuantos(bosque, tipo_de_celda, debug = False):
    contador = 0
    for i in range (len(bosque)):
        if bosque [i] == tipo_de_celda:
            contador = contador + 1
    if debug:
        print (contador)
    return contador
# cuantos(brotes(generar_bosque(10), 80), 1)

#%% 04 RAYOS
def rayos(bosque, f, debug = False):
    for i in range (len(bosque)):
        rayo = suceso_aleatorio(f)
        if rayo == True and bosque[i] == 1:
            bosque[i] = -1
    if debug:
        print (bosque)
    return bosque
# rayos (brotes(generar_bosque(10), 80, True), 30, True)

#%% 05 PROPAGACION
def propagacion (bosque, debug = False):
    for i in range (len(bosque)):
        if bosque [i] == -1:
            if bosque [i + 1] == 1:
                bosque [i + 1] = -1
            if bosque [i - 1] == 1:
                bosque [i - 1] = -1
    if debug:
        print (bosque)
    return bosque
# propagacion(rayos (brotes(generar_bosque(10), 80), 30), True)

#%% 06 LIMPIEZA
def limpieza (bosque, debug = False):
    for i in range (len(bosque)):
        if bosque [i] == -1:
            bosque [i] = 0
    if debug:
        print (bosque)
    return bosque
# limpieza (propagacion(rayos (brotes(generar_bosque(10), 80), 30), True), True)

#%% 07 PROGRAMA
def dinamica (n, a, p, f, debug = False):
    arboles = [] * a
    contador = 0
    while contador < a:
        bosque = generar_bosque (n)
        bosque_b = brotes(bosque, p)
        bosque_r = rayos (bosque_b, f)
        bosque_l = limpieza (bosque_r)
        vivos = cuantos (bosque_l, 1)
        arboles.append (vivos)
        contador = contador + 1
    promedio = sum (arboles) / a
    if debug:
        print (promedio)
    return promedio

def promedios (n, a, p, f):
    promedios = []* a
    contador = 0
    while contador <= 10:
        promedios.append(dinamica (n, a, p, f))
        contador = contador + 1
        p = p + 10
    print(promedios)
    return promedios
lista_promedios = promedios(100, 1000, 0, 2)

plt.title("titulo del grafico")
plt.xlabel("valores de x", fontsize = 16)
plt.ylabel("valores de y", color = "blue")
plt.plot(lista_promedios, ".")
plt.show()


# ax.lista_promedios
# plt.savefig('diagrama-dispersion.png')
# plt.show()
