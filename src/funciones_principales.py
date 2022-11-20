from collections import namedtuple
from datetime import datetime
import csv

Vigilancia=namedtuple("Vigilancia","fecha, genero, edad, ciudad, patogeno")

def lee_fichero_vigilancia(nombre_fich):
    print("\tLectura de pacientes: ")
    lista=[]
    with open(nombre_fich) as f:
        lector=csv.reader(f, delimiter=";")
        next(lector)
        for fecha, genero, edad, ciudad, patogeno in lector:
            edad=int(edad)
            fecha1=datetime.strptime(fecha, '%d/%m/%Y').date()
            tupla=Vigilancia(fecha1, genero, edad, ciudad, patogeno)
            lista.append(tupla)
    return lista

def condicion_patogeno(lista, Patogeno):
    res=[t for t in lista if t.patogeno==Patogeno]
    return res

def media_edad(lista, Ciudad):
    lista_auxiliar=[t.edad for t in lista if t.ciudad==Ciudad]
    suma=sum(lista_auxiliar)
    elem=len(lista_auxiliar)
    return suma/elem

def hombres_mayor_edad(lista, Genero, n=10):
    lista_auxiliar=[t for t in lista if t.genero==Genero]
    lista_auxiliar.sort(key=lambda x:x.edad, reverse=True)
    lista_ciudad=[t.ciudad for t in lista_auxiliar]
    res=[] 
    for i in lista_ciudad:
        if i not in res:
            res.append(i)
    return res[:n]

def mujer_mas_edad(lista, Genero):
    lista_aux=[t for t in lista if t.genero==Genero]
    tupla_max=max(lista_aux, key=lambda x:x.edad)
    return tupla_max.edad

def mujer_mas_edad_ciudad(lista, Genero, Ciudad):
    lista_aux=[t for t in lista if t.genero==Genero and t.ciudad==Ciudad]
    tupla_max=max(lista_aux, key=lambda x:x.edad)
    return tupla_max.edad