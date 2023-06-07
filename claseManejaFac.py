import csv
from claseFac import *
from claseCarr import *

class ManejaFac:
    def __init__(self):
        self.__facultades=[]

    def addFac(self, fac):
        self.__facultades.append(fac)

    def addCar(self, carrera, i):
        self.__facultades[i].addCarrera(carrera, 1)

    def archivero(self):
        archivo=open("Facultades.csv")
        i=0
        linea=archivo.readline()
        while linea != '':
            elem = linea.split(',')
            cod=elem[0]
            nom=elem[1]
            direc=elem[2]
            loc=elem[3]
            tel=elem[4]
            facultad=Facultad(cod, nom, direc, loc, tel)
            self.addFac(facultad)
            linea = archivo.readline()
            if (linea != ''):
                elem2 = linea.split(',')
                while (elem2[0]==cod):
                    codC=elem2[1]
                    nomC=elem2[2]
                    tit=elem2[3]
                    dura=elem2[4]
                    nivel=elem2[5]
                    carrera=Carrera(codC, nomC, dura, tit, nivel)
                    self.addCar(carrera, i)
                    linea = archivo.readline()
                    elem2=linea.split(',')
            i=i+1
        archivo.close()

    def getcod2(self, i):
        return self.__facultades[i].getcod()

    def buscaFacCod(self, cod):
        n=0
        i=0
        retorna=None
        while((n<len(self.__facultades))and(self.getcod2(i) != cod)):
            n=n+1
        if (n<len(self.__facultades)):
            retorna=i
        else:
            retorna=-1
        return retorna

    def getNomfac(self, i):
        return self.__facultades[i].getNF()

    def getLoc(self, i):
        return self.__facultades[i].getlocal()

    def getCarFac(self, i):
        return self.__facultades[i].getcarrera()

    def listaCarreras(self, i):
        n=1
        for carrera in (self.__facultades[i].getcarrera):
            nom=carrera.getNom()
            dura=carrera.getDuracion()
            print("Carrera {}:".format(n))
            print("Nombre de la carrera: {}".format(nom))
            print("Duracion de la carrera: {}".format(dura))
            n=n+1

    def getCodCar(self, n, i):
        carrera=self.__facultades[n].getcarrera
        cod=carrera[i].getCodC
        return cod

    def buscaFacNomCar(self, nom):
        n=0
        bandera=True
        i1=0
        retorna = None
        while ((n< len(self.__facultades)) and (bandera == True)) :
            i=0
            carreras=self.getCarFac(n)
            while ((carreras[i].getNom != nom)and(i<len(carreras))):
                i=i+1
            if (carreras[i].getNom == nom):
                bandera=False
                i1=i
            n=n+1
        if (bandera==False):
            codf=str(self.getcod2(n))
            codc=str(self.getCodCar(n, i1))
            codT= codf + codc
            print("Codigo: {}".format(codT))
            retorna=n
        else:
            retorna=-1
        return retorna









