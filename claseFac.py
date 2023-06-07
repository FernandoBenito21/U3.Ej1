from claseCarr import *
from claseManejaFac import *

class Facultad:
    __carrera=list
    def __init__(self, cod, nom, dir, loc, tel, carrera=None):
        self.__cod=cod
        self.__nom=nom
        self.__dir=dir
        self.__loc=loc
        self.__tel=tel
        if carrera != None:
            self.addCarrera(carrera)

    def getcod(self):
        return self.__cod

    def getNF(self):
        return self.__nom

    def getcarrera(self):
        return self.__carrera

    def getlocal(self):
        return self.__loc

    def addCarrera(self, carrera):
        self.__carrera().append(carrera)


