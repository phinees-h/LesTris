Ce projet contient quelques fonctions de ti sur les
liste en Python3:

Tri par insertion:
L’idée est de trier progressivement le tableau : supposant que t [0 : k] est déjà trié, j’insère t [k] à sa place
parmi les valeurs de t [0 : k] (en décalant les plus grandes valeurs d’un cran vers la droite si nécessaire)
de sorte que t [0 : k + 1] se retrouve trié.

Fichier : tri.py
1/ Version itérative : tri_insertion_iteratif
2/ Version récursive : insere et tri_ins_recursif

Fichier tester_tri.py
Contient les tests des fonctions de tri écrit dans le fichier tri.py

