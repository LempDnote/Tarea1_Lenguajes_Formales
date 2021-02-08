if __name__ == '__main__':
    N = int(raw_input())
    numeros = []
    for i in range(0,N):
        entrada = raw_input()
        instruccion = entrada.split()
        if instruccion[0] == "insert":
            numeros.insert(int(instruccion[1]),int(instruccion[2]))
        if instruccion[0] == "print":
            print(numeros)
        if instruccion[0] == "remove":
            numeros.remove(int(instruccion[1]))
        if instruccion[0] == "append":
            numeros.append(int(instruccion[1]))
        if instruccion[0] == "sort":
            numeros.sort()
        if instruccion[0] == "pop":
            numeros.pop()
        if instruccion[0] == "reverse":
            numeros.reverse()