ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrarPoliAlfabetico(message, key):
    newMessage = ""
    for i in range(len(message)):
        newMessage += ABC[(ABC.find(message[i]) + ABC.find(key[i % len(key)])) % len(ABC)]
    return newMessage

def descifrarPoliAlfabetico(message, key):
    newMessage = ""
    for i in range(len(message)):
        newMessage += ABC[(ABC.find(message[i]) - ABC.find(key[i % len(key)])) % len(ABC)]
    return newMessage

if __name__ == "__main__":
    m = input("Ingrese un mensaje: ")
    k = input("ingrese la clave: ")
    n = cifrarPoliAlfabetico(m, k)
    print(n)
    print(descifrarPoliAlfabetico(n, k))