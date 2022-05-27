import random

MESSAGE = "MIMAMAMEMIMA"

GROUPS = {
    'M': ["0000", "0100", "1000", "1100"],
    'A': ["0001", "0101", "1001", "1101"],
    'E': ["0010", "0110", "1010", "1110"],
    'I': ["0011", "0111", "1011", "1111"],
}

def cifrarHomofono():
    newMessage = ""
    for i in range(len(MESSAGE)):
        listOfValues = GROUPS.get(MESSAGE[i])
        newMessage += listOfValues[random.randint(0, len(listOfValues) - 1)]
    return newMessage

def descifrarHomofono(cifrado):
    newMessage = ""
    for i in range(0, len(cifrado), 4):
        x = cifrado[i:i + 4]
        for key, value in GROUPS.items():
            if value.count(x):
                newMessage += key
    return newMessage

if __name__ == "__main__":
    print("Cifrar y descifrar MIMAMAMEMIMA 5 veces:")
    a = cifrarHomofono()
    b = cifrarHomofono()
    c = cifrarHomofono()
    d = cifrarHomofono()
    e = cifrarHomofono()
    print(a, descifrarHomofono(a))
    print(b, descifrarHomofono(b))
    print(c, descifrarHomofono(c))
    print(d, descifrarHomofono(d))
    print(e, descifrarHomofono(e))
