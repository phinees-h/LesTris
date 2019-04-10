def tri_insertion_iteratif(tab):
    taille = len(tab)
    for i in range(taille):
        temp=tab[i]
        j=i
        while j>0 and temp<tab[j-1]:
            tab[j]=tab[j-1]
            j-=1
        tab[j]=temp
    return tab
