SList = [[], [], [], []]

def fillList(message):
    for i in range(len(message)):
        if i % 5 == 0:
            SList[0].append(i)
        elif i % 3 == 0:
            SList[1].append(i)
        elif i % 2 == 0:
            SList[2].append(i)
        else:
            SList[3].append(i)

def cifrarPorSeries(message):
    fillList(message)
    newMessage = ""
    for myList in SList:
        for i in myList:
            newMessage += message[i]
    return newMessage

def descifrarPorSeries(cifrado):
    newMessage = ""
    completeList = []
    for myList in SList:
        for i in myList:
            completeList.append(i)
    for i in range(len(completeList)):
        newMessage += cifrado[completeList.index(i)]
    return newMessage


if __name__ == "__main__":
    x = cifrarPorSeries("HOLAMUNDO")
    print(x, descifrarPorSeries(x))
