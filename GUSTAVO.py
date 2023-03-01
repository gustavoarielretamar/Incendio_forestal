#%% LIBRERIAS
import random


#%% VARIABLES GLOBALES
bosque = []


#%% SUCESO ALEATORIO
def suceso_aleatorio (p, debug = False):
    suceso = False
    prob = random.randint(0, 100)
    if prob <= p:
        suceso = True
    if debug:
        print(suceso)
    return suceso

suceso_aleatorio (80, True)

#%% 01 GENERAR BOSQUE
def generar_bosque (n, debug = False):
    bosque = [0] * n
    if debug:
        print(bosque)
    return bosque

generar_bosque(10, True)

#%% 02 BROTES
def brotes (bosque, p, debug = False):
    bosque = generar