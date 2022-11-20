Para la realización de este proyecto, he empleado una función de lectura de fichero csv, para el cual he utilizado la función namedtuple. Con esta función conseguimos que se nos devuelva una lista de tuplas que contenga el contenido del fichero csv, llamado sistema_vigilancia.csv

Función:

def lee_fichero_vigilancia(nombre_fich):
    print("\tLectura de pacientes: ")
    lista=[]
    with open(nombre_fich) as f:
        lector=csv.reader(f, delimiter=";")
        next(lector)
        for fecha, genero, edad, ciudad, patogeno in lector:
            fecha1=datetime.strptime(fecha, '%d/%m/%Y').date()
            tupla=Vigilancia(fecha1, genero, edad, ciudad, patogeno)
            lista.append(tupla)
    return lista


En esta segunda entrega del proyecto, hemos implementado diferentes funciones:

    En primer lugar, una función que te devuelve una lista de tuplas igual que la original pero pero solo con aquellos registros que verifican una condición.
    A continuación, una función que devuelva la suma, promedio o un cálculo sobre las tuplas o parte de ellas. 
    En tercer lugar, una función que obtenga una lista con n registros ordenados de mayor a menor por un campo determinado de entre los que cumplan una condición.
    Lo siguiente ha sido una función que obtenga un máximo o un mínimo respecto a algún campo determinado. 
    Y por último, cualquier función del tipo de las funciones adicionales que explicaremos con el proyecto Nombres.
