from collections import namedtuple
from datetime import datetime
import csv
from funciones_principales import *

# Fecha;Genero;Edad;Ciudad;Patogeno
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

def test_condicion_patogeno(lista):
    print("-----Obtener una lista de tuplas igual que la original pero solo con aquellos registros que verifican una condición:")
    lista_p=condicion_patogeno(lista, "VIRUELA_MONO")
    print("Lista de infectados por viruela del mono:") 
    print(lista_p)

def test_media_edad(lista):
    print("-----Una función que devuelva la suma, promedio o un cálculo sobre las tuplas o parte de ellas:")
    Ciudad="Sevilla"
    media=media_edad(lista, Ciudad)
    print(f"La media de edad en {Ciudad} de todos los patógenos es de:{media}")

def test_hombres_mayor_edad(lista):
    print("-----Función que obtenga una lista con n registros ordenados de mayor a menor por un campo determinado de entre los que cu0mplan una condición:")
    n=5
    Genero="Male"
    Ciud=hombres_mayor_edad(lista, Genero, n)
    print(f"Los hombres más mayores en orden de su Ciudad: {Ciud}")

def test_mujer_mas_edad(lista):
    print("-----Función que obtenga un máximo o un mínimo respecto a algún campo determinado:")
    Genero="Female"
    Ed=mujer_mas_edad(lista, Genero)
    print(f"La mujer con más edad que padece una enfermedad es de: {Ed} años")

def test_mujer_mas_edad_ciudad(lista):
    print("-----Función adicional:")
    Genero="Female"
    Ciudad="Sevilla"
    May=mujer_mas_edad_ciudad(lista, Genero, Ciudad)
    print(f"La mujer con más edad que padece una enfermedad en {Ciudad} es de: {May} años")



if __name__=="__main__":
    res=lee_fichero_vigilancia('./data/sistema_vigilancia.csv')
    print(res)
    test_condicion_patogeno(res)
    test_media_edad(res)
    test_hombres_mayor_edad(res)
    test_mujer_mas_edad(res)
    test_mujer_mas_edad_ciudad(res)






