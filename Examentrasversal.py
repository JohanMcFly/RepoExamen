juegos={
 'G001': ["Eclipse Runner", "PC", "accion", "T", True,
'NovaStudio'],
 'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
 'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
 'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
 'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
 'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate'],
 "G006": ["Mario Bros 2", "Switch","aventura", "E", False, "Nintendo"],
 "G007": ["Sonic 2", "PC", "aventura", "E", False,"Sega"],
 "G008": ["Pokemon Black", "Switch", "accion", "E", True, "GameFreak"]
}
inventario={

"G001": [9990,7],
"G002": [19990,0],
"G003": [42990,3],
"G004": [14990,5],
"G005": [17990,9],
"G006": [39990,2],
"G007": [20000,2],
"G008": [40000,1],
}
def leer_opcion():
    opcion = int(input("Ingrese una opcion: "))
    if opcion < 7:
        print ("Opcion Valida")
    else:
        print("opcion invalida")
    return opcion

def stock_plataforma(plat):
    stock_total = 0
    plat_lower = plat.lower
    for codigo, datos in juegos.items():
        if datos[1].lower() == plat_lower:
            stock == inventario[codigo][1]
            stock_total += stock
    print (f"El stock es de {stock_total}")

def actualizar_juegos(codigo,nuevo_precio):
    if codigo in inventario[codigo]:
        nuevo_precio == inventario[codigo][0]
        print (f"Se remplazo el precio de {codigo}")
    else:
        print ("No se encontro el juego")
        
def busqueda_precio(p_min,p_max):
    for codigo, datos in juegos.items():
        if inventario[codigo][0] >= p_min and inventario[codigo][0] <= p_max:
            print (f"Se encontraron los siguientes juegos")
            print (f"{juegos[codigo][0]} {inventario[codigo][0]}")
    
def agregar_juego(codigo):
  for codigo in juegos.items():  
    if codigo != juegos:
        codigo_new = input("Ingrese el Codigo del juego que desea agregar")
        if codigo_new != ("") or codigo_new != codigo:
            titulo = input("ingrese el nombre del juego")
            if titulo  != ("") or titulo != (" "):
                plataforma_new = input ("Ingrese la plataforma del juego")
                if plataforma_new != ("") or plataforma_new !=(" "):
                    clasificacion_new = input("Ingrese la clasificacion del juego (E).(T).(M)")
                    if clasificacion_new == ("E") or clasificacion_new == ("T") or clasificacion_new == ("M"):
                        Multiplayer_New = input("Ingrese si el juego es multiplayer o no (S/N)")
                        if Multiplayer_New == ("S"):
                            Multiplayer_New == True
                        elif Multiplayer_New == ("N"):
                            Multiplayer_New == False
                            editor_new = input("Ingrese el editor del juego")
                            if editor_new != (" ") and editor_new != (""):
                                precio = int(input("Ingrese el precio del juego"))
                                if precio > 0 and precio != (float):    
                                    stock = int(input("Ingrese el Stock del juego"))
                                    if stock >= 0:
                                        juegos[0,1,2,4,5]
                                        inventario.add(precio,stock)
                                    else:
                                        print("Stock invalido")
                                else:
                                    print("precio invalido")
                                    
                            else:
                                print("Editor invalido")
                        else:
                         print("Opcion invalida")
                    else:
                        print("Clasificacion invalida")
                else:
                    print("plataforma invalida")
            else:
                print("Titulo invalido")
        else:
            print("Codigo invalido")
    else:
        print("ese codigo ya existe")
def buscar_codigo(codigo):
    if codigo in juegos:
        print ("Se encontro el codigo")
        return codigo
def eliminar_juego(codigo):
    for codigo,datos in juegos.items():
        if inventario[codigo][0] == codigo:
            print ("Quiere borrar el juego de la tienda ?(S/N)")
            borrar = int(input("Ingrese su eleccion"))
            if borrar == "S":
                inventario[codigo].remove
                juegos[codigo].remove
                print ("Se borro el juego con exito")
            if borrar == "N":
                print ("Se cancelo la eliminacion")

while True:
    try:
        print("Bienvenido al Menu")
        print ("1- Stock por plataforma\n 2- Busqueda de juegos por rango de precio\n 3- Actualizar precio de los juegos \n 4- Agregar Juego\n 5- Eliminar Juego\n 6-Salir")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            plat = input("Ingrese el nombe de la plataforma que desea buscar: ")
            stock_plataforma(plat)
        elif opcion == 2:
            p_min = int(input("Ingresa el precio minimo"))
            p_max = int(input("Ingresa el precio maximo"))
            busqueda_precio(p_min,p_max)

        elif opcion == 3:
            codigo = input("input ingresa el codigo que deseas buscar")
            buscar_codigo(codigo)
            nuevo_precio = int(input("ingrese el precio nuevo del juego"))
            actualizar_juegos(codigo,nuevo_precio)
        elif opcion == 4:
            codigo = input("Ingrese el Codigo que desea buscar")
            buscar_codigo(codigo)
            agregar_juego(codigo)
        elif opcion == 5:
            codigo = input("Ingrese que codigo desea buscar: ")
            buscar_codigo(codigo)
            eliminar_juego(codigo)
        elif opcion == 6: 
            print("Adios")
            break
    except ValueError:
        print("Opcion invalida")