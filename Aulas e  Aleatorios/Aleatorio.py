listanum = [0,5,5,6,6,6,7]
print(listanum)
listapos = []
for n in listanum:
    if n % 2 ==0:
        listapos.append(listanum.index(n))
print(listapos)