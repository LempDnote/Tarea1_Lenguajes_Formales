if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    listado = list(arr)
    listado.sort()
    listado.reverse()

    for i in range(len(listado)):
        if(listado[i+1] < listado[i]):
            print(listado[i+1])
            break