mi_lista = [10, 20, 30, 40, 50]
def ejecicio1(lista, elemento):
    if not lista:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return ejecicio1(lista[1:], elemento)

#elemento_buscado = 40

#if ejecicio1(mi_lista, elemento_buscado):
#    print("Se encontró el elemento en la lista.")

#else:
#    print("No se encontró el elemento en la lista.")

#___________________
def direction(home=1):
    print(f"Hola Seven, mi dirección de casa es: {home}")

#direccion("Calle Melchor Rodriguez")

def direction(mail):
    print(f"Hola Seven, envíame la información a este correo: {mail}")

#direccion()

#_________________

def sum(*args):
    value = 0
    for n in args:
        value += n
    return value

#resultado = sum(1000, 210, 20, 40,233, 34,6,89)
#print(resultado)

#_______________
ciudad= {"Madrid":1}
def filter(**kwargs):
    query = "SELECT * FROM clientes"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "

        query += "{}='{}'".format(key, value)
        i += 1

    query += ";"
    return query

filter(ciudad="Madrid")

