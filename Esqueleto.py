Contraseña=''
intentos=0
Precio_total=0
Resumen_de_productos = ''
while intentos < 3 and Contraseña != 'OXXO':
    Contraseña=input("Ingrese la contraseña: ")
    if Contraseña=='OXXO':
        Producto_totales=int(input("Ingrese la cantidad del producto: "))
        Presupuesto = float(input("Ingrese el presupuesto total: "))
        opcion=int(input("Ingrese 1 para agregar un producto o 2 para eliminar producto: "))
        for i in range(Producto_totales):
            if opcion==1:
                Nombre_del_producto=input("Ingrese el nombre del producto: ")
                Precio_del_producto=float(input("Ingrese el precio del producto: "))
                Cantidad_del_producto=int(input("Ingrese la cantidad del producto: "))
        Resumen_de_productos+='Producto: '+Nombre_del_producto+', Precio: '+str(Precio_del_producto)+', Cantidad: '+str(Cantidad_del_producto)+'\n'
        Precio_total+=Precio_del_producto*Cantidad_del_producto
        if Precio_total > Presupuesto:
            print("El presupuesto no es suficiente para este producto.")
        elif opcion==2:
            continue
    else:
        print("Contraseña incorrecta. No se pueden agregar o eliminar productos.")
        intentos += 1
print(Resumen_de_productos)
print("El precio total es: ", Precio_total)