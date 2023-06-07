from claseFac import *

class Carrera:
    def __init__(self, cod, nom, dura, titulo, nivel):
        self.__cod=cod
        self.__nom=nom
        self.__duracion=dura
        self.__titulo=titulo
        self.__nivel=nivel

    def getDuracion(self):
        return self.__duracion

    def getNom(self):
        return self.__nom

    def getCodC(self):
        return self.__cod
