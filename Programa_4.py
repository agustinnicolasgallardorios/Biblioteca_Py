print("bienvenidos al contador de biblioteca")

client = input("ingrese el nombre del cliente ")
id_lib = input("ingrese el id del libro ")
nrostock = input("ingrese el nro de stock ")

class biblioteca:
    def __init__(self, cliente, id_libro, nro_stock):
        self.cliente = cliente
        self.id_libro = id_libro
        self.nro_stock = nro_stock
    
    def cartelera (self):
        print("el nombre del cliente sera ", self.cliente)
        print("la identificacion del libro sera ", self.id_libro)
        print("el nro de stock, es el siguiente ", self.nro_stock)

cart = biblioteca(client, id_lib, nrostock)
cart.cartelera()

confirmacion = input("¿confirma que es correcto?")

pos= "si"
neg= "no"

cuenta_reg = 0

while cuenta_reg < 2:

    if confirmacion == pos:
        print("Buenisimo, que tenga un excelente dia!")
        break
    elif confirmacion == neg:
        client = input("ingrese nuevamente el nombre del cliente ")
        id_lib = input("ingrese nuevamente el id del libro ")
        nrostock = input("ingrese nuevamente el nro de stock ")
        cart = biblioteca(client, id_lib, nrostock)
        cart.cartelera()
        confirmacion_nva = input("asegurese, si finalmente, son correctos esos datos ")
    else:
        print("usted no confirmo nada, hasta luego")
        break


    if confirmacion_nva == pos:
        print("los datos son correctos, buenisimo, que tenga un buen dia")
        break
    elif confirmacion_nva == neg:
        print("Contactese al numero 234 - 5897, un personal le ofrecera un turno presencial")
    else:
        print("usted no confirmo nada, hasta luego")
        break
    