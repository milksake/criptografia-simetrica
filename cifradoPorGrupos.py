
def cifrarPorGrupos(message, key):
    m = message
    newMessage = ""
    if len(message) % len(key) != 0:
        m += '\0' * (len(key) - (len(message) % len(key)))
    for i in range(0, len(m), len(key)):
        substr = m[i : i + len(key)]
        for j in key:
            newMessage += substr[int(j)]
    return newMessage

def descifrarPorGrupos(message, key):
    newMessage = ""
    for i in range(0, len(message), len(key)):
        substr = message[i : i + len(key)]
        for j in range(len(key)):
            newMessage += substr[key.find(str(j))]
    return newMessage


if __name__ == "__main__":
    key = "201"
    x = cifrarPorGrupos("HOLAMUNDO", key)
    print(x, descifrarPorGrupos(x, key))
