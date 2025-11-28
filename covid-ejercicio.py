#Ejercicio: Registro de personas con COVID en zonas rurales
#Enunciado:
#Crea un programa en Python que permita registrar personas contagiadas 
#por COVID en diferentes poblaciones rurales. El programa debe permitir:
#1.Agregar personas con sus datos.
#2.Eliminar registros por nombre.
#3.Mostrar la lista completa.
#Calcular el porcentaje de infectados respecto al total registrado.
#Cada persona debe guardarse como un diccionario, y todos los registros deben almacenarse en una lista.""
#datos persona:nombre edad sexo ciudad y temperatura"
def menu():
    
    print("Bienvenido al registro de personas con COVID en zonas rurales")
    print("/////////////////////////////////////////////////////////////")
    print("-----MENÚ-----")
    print("1.Agregar personas con sus datos.")
    print("2.Eliminar registros por nombre.")
    print("3.Mostrar la lista completa.")
    print("4.Porcentaje de infectados respecto al total registrado.")
    print("5.Salir")

def agregar_persona(lista):
    nombre=input("Ingrese nombre :_")
    edad=int(input("Ingrese edad :_"))
    sexo=input("Ingrese sexo:_")
    ciudad=input("Ingrese ciudad:_")
    temperatura=float(input("Ingrese temperatura:_"))

    diccionario={"Nombre":nombre,"Edad":edad,"Sexo":sexo,"Ciudad":ciudad,"Temperatura":temperatura}
    lista.append(diccionario)

    print("Registro correcto.")
    return (lista)

def buscar_registro(lista):
    nombre=input("Nombre a buscar:_")
    for i in range (len(lista)):
        if nombre == lista[i]["Nombre"]:
            return(i)
        else:
            print("Nombre no registrado.")
 
def eliminar_registro(indice,lista):
    lista.pop(indice)
    print("Registro eliminado")
    return(lista)

def mostrar_lista(lista):
    print(lista)

def porcentaje(lista):
    fiebr=0
    cnt=len(lista)
    for i in range (cnt):
        if lista[i]["Temperatura"] >= 37.0:
            fiebr=fiebr+1
    prom=fiebr/cnt
    porcentaje=prom*100

    return(porcentaje)

def main():
    lista=[]
    menu()
    opc=int(input("Ingrese una opción:_"))
    while opc >= 1 and opc <= 5:

        if opc == 1:
            lista=agregar_persona(lista)
        if opc == 2:
            indice=buscar_registro(lista)
            lista=eliminar_registro(indice,lista)
        if opc == 3:
            mostrar_lista(lista)
        if opc == 4:
            porcenta=porcentaje(lista)
            print("El porcentaje de infectado es de",porcenta,"%")
        if opc == 5:
            print("SALIENDO *******")
            return
        menu()
        opc=int(input("Ingrese una opción:_"))

    else:
        print("El número ingresado no es una opción valida\n")
        menu()

main()