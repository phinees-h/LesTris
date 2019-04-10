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

#version récursive du tri par insertion
def insere(tab,j):
    if j>0 and tab[j]<tab[j-1]:
        tab[j-1],tab[j]=tab[j],tab[j-1]
        insere(tab, j-1)

def tri_ins_recursif(tab,j=1):
    if j<len(tab):
        insere(tab,j)
        tri_ins_recursif(tab,j+1)
