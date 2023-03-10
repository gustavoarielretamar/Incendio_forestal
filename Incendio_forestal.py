#%% LIBRERIAS
import random
import matplotlib.pyplot as plt

#%% 01 GENERAR BOSQUE:
def generar_bosque (n, debug = False):
    bosque = [0] * n
    if debug:
        print (bosque)
    return bosque
#%% SUCESO ALEATORIO:
def suceso_aleatorio (p, debug = False):
    suceso = False
    prob = random.randint(0, 100)
    if prob <= p:
        suceso = True
    if debug:
        print(suceso)
    return suceso
#%% 02 BROTES, genera brotes en un bosque usando suceso aleatorio:
def brotes(bosque, p, debug = False):
    for i in range (len(bosque)):
        brote = suceso_aleatorio(p)
        if brote == True:
            bosque[i] = 1
    if debug:
        print (bosque)
    return bosque
#%% 03 CUANTOS, cuenta cuanto hay del tipo de celda especificado:
def cuantos(bosque, tipo_de_celda, debug = False):
    contador = 0
    for i in range (len(bosque)):
        if bosque [i] == tipo_de_celda:
            contador = contador + 1
    if debug:
        print (contador)
    return contador
#%% 04 RAYOS, genera rayos en un bosque usando suceso aleatorio:
def rayos(bosque, f, debug = False):
    for i in range (len(bosque)):
        rayo = suceso_aleatorio(f)
        if rayo == True and bosque[i] == 1:
            bosque[i] = -1
    if debug:
        print (bosque)
    return bosque
#%% 05 PROPAGACION
def propagacion (bosque, debug = False):
    i = 0
    while i < (len(bosque) - 1):
        if bosque[i] == - 1 and bosque [i + 1] == 1:
            bosque [i + 1] = - 1
        i = i + 1
    i = len (bosque) -1
    while i != 0:
        if bosque [i] == - 1 and bosque [i - 1] == 1:
            bosque [i - 1] = -1
        i = i - 1
    if debug:
        print (bosque)
    return bosque
#%% 06 LIMPIEZA
def limpieza (bosque, debug = False):
    for i in range (len(bosque)):
        if bosque [i] == -1:
            bosque [i] = 0
    if debug:
        print (bosque)
    return bosque
#%% 07 PROGRAMA
def dinamica (n, a, p, f, debug = False):
    arboles = [] * a
    contador = 0
    while contador < a:
        bosque = generar_bosque (n)
        bosque_b = brotes(bosque, p)
        bosque_r = rayos (bosque_b, f)
        bosque_p = propagacion(bosque_r)
        bosque_l = limpieza (bosque_p,)
        vivos = cuantos (bosque_l, 1)
        arboles.append (vivos)
        contador = contador + 1
    promedio = sum (arboles) / a
    if debug:
        print (promedio)
    return promedio
# %% VALOR OPTIMO DE P:
def valor_optimo_de_p(n, a, p, f, debug = False):
    promedios = []* a
    contador = 0
    while contador <= 100:
        promedios.append(dinamica (n, a, p, f))
        contador = contador + 1
        p = p + 1
    if debug:
        print(promedios)
        
    return promedios
# %% PARAMETROS:
n = 100
p = 0
f = 2
a = 500
# %% LLAMADAS:
# generar_bosque (n, True)
# suceso_aleatorio(p, True)
# brotes(generar_bosque(n, True), p, True)
# cuantos(brotes(generar_bosque(n, True), p, True), 1, True)
# rayos (brotes(generar_bosque(n), p, True), f, True)
# b_1 = [1, 1, 1, -1, 0, 0, 0, -1, 1, 0]
# b_2 = [-1, 1, 1, -1, 1, 1, 0, 0, -1, 1]
# propagacion(b_1, True)
# propagacion(rayos (brotes(generar_bosque(n, True), p, True), f, True), True)
# limpieza (propagacion(rayos (brotes(generar_bosque(n, True), p, True), f, True), True), True)
# dinamica(n, a, p, f, True)
lista_promedios = valor_optimo_de_p(n, a, p, f, True)

plt.title("titulo del grafico")
plt.xlabel("valores de x", fontsize = 16)
plt.ylabel("valores de y", color = "blue")
plt.plot(lista_promedios, ".")
plt.show()
ax.lista_promedios
plt.savefig('diagrama-dispersion.png')
plt.show()
