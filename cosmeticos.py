import csv
import time
import os

def agregar_cosmetico():
    columnas = ("FOLIO", "DESCRIPCION", "CANTIDAD", "PRECIO_UNITARIO", "TOTAL_PRODUCTO", "FECHA")
    r = 1
    folio = 0
    lista = []
    listasuma = []
    while r == 1:
        f = "cosmeticos_csv.csv"
        ex = os.path.isfile(f)
        
        if ex:
            with open("cosmeticos_csv.csv", "r", newline="") as archivo:
                lector = csv.reader(archivo, delimiter = ",")
                next(archivo)
                lista_csv = list(lector)
                
        if folio == 0:
            if ex: 
                c = 0
                for e in lista_csv:
                    nfolio = lista_csv[c][0]
                    c = c+1
                nfolio = int(nfolio)
                folio = nfolio + 1
            else:
                folio = 1
        folio = int(folio)
        descripcion = input("Ingresa el nombre del articulo >>> ")
        cantidad = int(input("Ingresa la cantidad del articulo >>> "))
        punitario = int(input("Ingresa el precio unitario >>> "))
        ptotal = int(cantidad * punitario)
        fecha = (time.strftime("%Y-%m-%d"))

        datos = [[(folio), (descripcion), (cantidad), (punitario), (ptotal), (fecha)]]
        lista.append(datos)
        listasuma.append(ptotal)
        
        with open("cosmeticos_csv.csv", "w", newline="") as archivo:
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            if ex:
                registrador.writerows(lista_csv)
            registrador.writerows(datos)
        columnas = None
        datos = list()

        with open("cosmeticos_csv.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter = ",")
            registros = 0
            
            for folio, descripcion, cantidad, punitario, ptotal, fecha in lector:
                if registros == 0:
                     columnas = (folio, descripcion, cantidad, punitario, ptotal, fecha)
                     registros = registros + 1
                else:
                    datos.append([folio, descripcion, cantidad, punitario, ptotal, fecha])
        print("¿Desea registrar otro producto?")
        print("1.SI\t2.NO")
        r = int(input())
    print(f"Folio venta: {folio}")
    for lista_primer_nivel in lista:
        for elemento in lista_primer_nivel:
            print(f"{elemento}")
    Suma = 0
    for i in listasuma:
        Suma = Suma + i
    print(f"El total a pagar es {Suma}")
        
def consultar_venta():
    folioc = input("Ingrese el numero de folio >>> ")
    folioc = str(folioc)
    with open("cosmeticos_csv.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo, delimiter = ",")
        next(archivo)
        lista_csv = list(lector)
    e = 0
    listap = list()
    for n in lista_csv:
        if lista_csv[e][0] == folioc:
            listap.append(n)
        e = e+1
    print("FOLIO\tDESCR\tCANT\tPUNI\tTVENTA\tFECHA") 
    for lista_primer_nivel in listap:
        for elemento in lista_primer_nivel:
            print(f"{elemento}", end="\t")
        print("")
        
def consultar_fecha():
    print("Ingrese la fecha que desea consultar")
    fechac = input("AAAA-MM-DD >>> ")
    fechac = str(fechac)
    with open("cosmeticos_csv.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo, delimiter = ",")
        next(archivo)
        lista_csv = list(lector)
    e = 0
    listaf = list()
    for n in lista_csv:
        if lista_csv[e][5] == fechac:
            listaf.append(n)
        e = e+1
        
    print("FOLIO\tDESCR\tCANT\tPUNI\tTVENTA\tFECHA")    
    for lista_primer_nivel in listaf:
            for elemento in lista_primer_nivel:
                print(f"{elemento}", end="\t")
            print("")
            
def Menu_Principal():
    while True:
        print("1. Registrar una venta")
        print("2. Consultar venta")
        print("3. Consultar ventas por fecha")
        print("4. Salir")
        respuesta = int(input("Elige una opción :"))
        if respuesta == 1:
            agregar_cosmetico()
        elif respuesta == 2:
            consultar_venta()
        elif respuesta == 3:
            consultar_fecha()
        elif respuesta == 4:
            break
        else:
            print("OPCION NO VALIDA")


Menu_Principal()