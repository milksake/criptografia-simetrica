
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
    keyList = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        keyList.append(str(i) + str(j) + str(k) + str(l))
    for key in keyList:
        x = cifrarPorGrupos("HOLAMUNDO", key)
        print(x, descifrarPorGrupos(x, key))
