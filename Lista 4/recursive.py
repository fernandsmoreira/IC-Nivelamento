def soma(lista) :
    if len(lista) == 0 :
        return 0;
    else:
        head, *tail = lista
        return head + soma(tail)

soma([1,2,3])
