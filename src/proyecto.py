#Variables a mostrar
Contraseña=''
intentos=0
Producto=0
Opcion = ''

#---FUNCIONES PARA EL INVENTARIO---

#Esta funcion muestra el menu del programa
def Menu():
    print('\n--- MENÚ INVENTARIO ---')
    print('1. Mostrar inventario')
    print('2. Agregar producto')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Buscar producto')
    print('6. Presupuesto total')
    print('7. Venta')
    print('8. Salir')
    try:
        Opcion = int(input("Seleccione una opción: "))
        return Opcion
    except ValueError: 
        print("Opción inválida.")
        return 
        
#En esta función se lleva a cabo el manejo y guardado de archivos .txt con el inventario
def cargar_inventario(nombre_archivo):
    inventario = {}
    try:
        with open(f"{nombre_archivo}.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    nombre, codigo, stock, precio = datos
                    inventario[nombre] = {
                        "codigo": codigo,
                        "Stock": int(stock),
                        "precio": float(precio)
                    }
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")
        open(f"{nombre_archivo}.txt", "w").close()
    return inventario

#En esta funcion se lleva a cabo el manejo y guardado de archivos .txt con las ganancias
def cargar_ganancias(nombre_archivo):
    try:
        with open(f"{nombre_archivo}_ganancias.txt", "r") as f:
            return float(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0.0

#En esta funcion se guarda y carga el inventario
def guardar_inventario(nombre_archivo, inventario):
    with open(f"{nombre_archivo}.txt", "w") as f:
        for nombre, datos in inventario.items():
            f.write(f"{nombre},{datos['codigo']},{datos['Stock']},{datos['precio']}\n")

#En esta funcion se cargan y guardan las ganancias
def guardar_ganancias(nombre_archivo, ganancias, prod=None, datos=None):
    if prod:
        with open(f"{nombre_archivo}_ganancias.txt", "a") as f:
            f.write(f"{prod}: {datos['cantidad']} unidades ${datos['subtotal']:.2f}\n")
    else:
        with open(f"{nombre_archivo}_ganancias.txt", "a") as f:
            f.write(f"Venta total: ${ganancias:.2f}")

#Con esta funcion se mostrara el producto con su respectiva informacion
def layout(nombre, datos):
    print(f"Producto: {nombre:<15} Código: {datos['codigo']:<10} Stock: {datos['Stock']:<5} Precio: ${datos['precio']:<8.2f}")

#Esta funcion es para agregar productos nuevos
def AgregarProducto(diccionario, archivo):
    nombre = input('Ingrese el nombre del producto: ').lower().strip()
    if nombre in diccionario: 
        print('El producto ya existe.')
        return
    codigo = input('Ingrese el código: ')
    for datos in diccionario.values():
        if datos['codigo'] == codigo:
            print('Ya existe un producto con ese código.')
            return
    try:
        stock = int(input('Ingrese stock: '))
        precio = float(input('Ingrese precio unitario: '))
        diccionario[nombre] = {'codigo': codigo, 'Stock': stock, 'precio': precio}
        print('Producto agregado.')
        guardar_inventario(archivo, diccionario)
    except ValueError: 
        print('Stock y precio deben ser numéricos.')

#Con esta funcion se va a mostrar el inventario
def MostrarInventario(diccionario):
    if not diccionario:
        print('Inventario vacío.')
    else:
        print('\n--- Inventario ---')
        print("{:<11}{:<10}{:<10}{:<10}".format('Producto:','Código:','Stock:','Precio Unitario:'))
        for nombre, datos in diccionario.items(): 
            print('{:<11}{:<10}{:<10}${:<10}'.format(nombre,datos['codigo'],datos['Stock'],datos['precio']))


#Esta funcion es para poder actualizar el invemtario
def ActualizarProducto(diccionario, archivo, dato=None, nuevo_stock=None):
    if dato is None:
        dato = input("Ingrese producto a actualizar: ").lower().strip()
    if dato in diccionario:
        try:
            if nuevo_stock is None:
                nuevo_stock = int(input("Ingrese nuevo stock: "))
            diccionario[dato]['Stock'] = nuevo_stock
            print('Producto actualizado.')
            guardar_inventario(archivo, diccionario)
            return True
        except ValueError:
            print('El stock debe ser numerico.')
            return False
    else:
        print('No encontrado.')
        return False
  
#Con esta función se podran eliminar productos
def EliminarProducto(diccionario, archivo):
    dato = input("Ingrese producto a eliminar: ").lower().strip()
    if dato in diccionario:
        diccionario.pop(dato)
        print('Producto eliminado')
        guardar_inventario(archivo, diccionario)
    else:
        print('Producto no encontrado')

#Esta funcion es para poder buescar un producto junto con sus datos
def BuscarProducto(diccionario,dato=None):
    if dato is None:
        dato = input('Ingrese producto o código a buscar: ').lower().strip()
    encontrado = False
    for nombre, datos in diccionario.items():
        if nombre == dato or datos['codigo'] == dato:
            print('Encontrado:')
            layout(nombre, datos)
            encontrado = True
    if not encontrado:
        print('No encontrado.')
    return encontrado

#Esta funcion es para el calculo final de los precios
def Preciototal(diccionario, ganancias_totales):
    #Esto es solo de ganancias de las ventas
    valor_inventario = sum(diccionario[p]['Stock'] * diccionario[p]['precio'] for p in diccionario)
    
    print(f"\n--- PRESUPUESTO TOTAL ---")
    print(f"Valor del inventario (no es ganancia): ${valor_inventario:.2f}")
    print(f"Ganancias por ventas realizadas: ${ganancias_totales:.2f}")
    print(f"TOTAL GENERAL (solo ganancias): ${ganancias_totales:.2f}")
    
    return ganancias_totales #son solo las ganancias

#Esta funcion registrara las ventas
def venta(diccionario, archivo, ganancias_acumuladas):
    carrito = {}
    total_venta = 0
    while True:
        dato = input("Ingrese producto o código a vender (o 'salir' para terminar): ").lower().strip()
        if dato.lower().strip() == 'salir':
            break
        
        nombre_encontrado = None
        for nombre, datos in diccionario.items():
            if nombre == dato or datos['codigo'] == dato:
                nombre_encontrado = nombre
                break
        
        if not nombre_encontrado:
            print("Ese producto no existe en el inventario.")
            continue
        try:
            cantidad = int(input(f"Ingrese cantidad de '{nombre_encontrado}': "))
        except ValueError:
            print('Debe ser un número.')
            continue
        
        if cantidad <= 0:
            print("Cantidad inválida.")
            continue
        
        stock_actual = diccionario[nombre_encontrado]['Stock']
        if cantidad > stock_actual:
            print(f"Stock insuficiente (disponible: {stock_actual}).")
            continue
        
        #Aqui resta lo vendido para actualizar el inventario
        nuevo_stock = stock_actual - cantidad
        diccionario[nombre_encontrado]['Stock'] = nuevo_stock
        
        #Calcular las ganancias de cada venta
        precio_venta = diccionario[nombre_encontrado]['precio']
        subtotal = cantidad * precio_venta
        total_venta += subtotal
        
        #Agregar al carrito
        carrito[nombre_encontrado] = {'cantidad': cantidad, 'subtotal': subtotal}
        print(f"{cantidad} {nombre_encontrado} añadido al carrito. Subtotal: ${subtotal:.2f}")
    if carrito:
        print("\n--- RESUMEN DE VENTA ---")
        for prod, datos in carrito.items():
            guardar_ganancias(archivo, ganancias_acumuladas, prod, datos)
            print(f"{prod}: {datos['cantidad']} unidades → ${datos['subtotal']:.2f}")
        
        print(f"Total de la venta: ${total_venta:.2f}")
        
        #Sumar las ganancias de esta venta a las ganancias acumuladas
        ganancias_acumuladas += total_venta
        print(f"Ganancias acumuladas actualizadas: ${ganancias_acumuladas:.2f}")
        
        print("\n--- INVENTARIO ACTUALIZADO ---")
        MostrarInventario(diccionario)
        
                #aqui se guardan los cambios
        guardar_inventario(archivo, diccionario)
        guardar_ganancias(archivo, ganancias_acumuladas)
        
        carrito.clear()
        print('Venta finalizada.')
    else:
        print('No se vendió nada.')
    
    return ganancias_acumuladas


# ===== Programa principal =====
Contraseña = ''
intentos = 0
Opcion = 0

nombre_archivo = input('¿Qué nombre tiene el archivo?: ').strip()
Productos = cargar_inventario(nombre_archivo)

#aqui carga las ganancias acumuladas
ganancias_totales = cargar_ganancias(nombre_archivo)
print(f"Ganancias acumuladas cargadas: ${ganancias_totales:.2f}")

while intentos < 3:
    Contraseña = input("Ingrese la contraseña: ")
    if Contraseña == 'OXO':
        while True: 
            Opcion = Menu()
            
            if Opcion is None: 
                continue
            
                
            if Opcion == 1:
                MostrarInventario(Productos)
            elif Opcion == 2:
                AgregarProducto(Productos, nombre_archivo)
            elif Opcion == 3:
                ActualizarProducto(Productos, nombre_archivo)
            elif Opcion == 4:
                EliminarProducto(Productos, nombre_archivo)
            elif Opcion == 5:
                BuscarProducto(Productos)
            elif Opcion == 6:
                Preciototal(Productos, ganancias_totales)
            elif Opcion == 7:
                ganancias_totales = venta(Productos, nombre_archivo, ganancias_totales)
            elif Opcion == 8:
                print('Saliendo...')
                guardar_inventario(nombre_archivo, Productos)
                guardar_ganancias(nombre_archivo, ganancias_totales)
                break
        break  
    else:
        print("Contraseña incorrecta.")
        intentos += 1
        if intentos >= 3: 
            print("Demasiados intentos fallidos. Saliendo del programa.") #Mensaje en caso de que hayan demaciados intentos fallidos
            break