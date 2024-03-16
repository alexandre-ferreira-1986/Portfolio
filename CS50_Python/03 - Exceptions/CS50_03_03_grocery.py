lista = list()

while True:
    try:
        item = input()
        if item != "":
            lista.append(item.upper())
    
        elif item == "":
            set_lista = set(lista)
            for i in set(set_lista):
                total = lista.count(i)
                print(f'{total} {i}')
            break
        
    except EOFError:
        pass