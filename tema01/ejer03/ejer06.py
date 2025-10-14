def imprimir_producto():
    
    nombre = input("Introduce tu nombre: ")
    producto = input("Introduce producto: ")
    precio = input("Introduce su precio: ")

    print(f"{nombre}, gracias por tu compra. El producto {producto} tiene un precio de {precio}€")

    print("{}, gracias por tu compra. El producto {} tiene un precio de {}€".format(nombre, producto, precio))

    print(nombre,", gracias por tu compra. El producto",producto,"tiene un precio de",precio,"€",sep="-")

if __name__ == "__main__":
    imprimir_producto()