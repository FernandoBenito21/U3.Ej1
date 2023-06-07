from claseFac import *
from claseCarr import *
from claseManejaFac import *

def Menu():
    print("...Menu...")
    print("0).Concluir")
    print("1).Listar carreras por facultad")
    print("2).Buscar facultad por carrera")

if __name__ == '__main__':
    facultades=ManejaFac()
    Menu()
    opcion = int(input('Ingresar opcion:'))
    while(opcion != 0):
        if (opcion==1):
            cod=int(input('Ingresar el codigo de la facultad:'))
            pos=facultades.buscaFacCod(cod)
            if (pos != -1):
                nom=facultades.getNomfac(pos)
                print("Para la facultad: {}, las carreras son:".format(nom))
                facultades.listaCarreras(pos)
            else:
                print("No se encontro una facultad con ese codigo")
        else:
            nom=input('Ingresar nombre de la carrera:')
            pos=facultades.buscaFacNomCar(nom)
            if (pos != -1):
                nomf=facultades.getNomfac(pos)
                locf=facultades.getLoc(pos)
                print("Nombre de la facultad: {}, localidad: {}".format(nomf, locf))

            else:
                print("No existe esa carrera")

        Menu()
        opcion = int(input('Ingresar opcion:'))
