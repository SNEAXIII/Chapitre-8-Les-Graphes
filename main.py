from jtape_au_sud import *

##Parcours DFS

chateau = Graphe()
chateau.ajouterArete('A', 'B')
chateau.ajouterArete('A', 'D')
chateau.ajouterArete('D', 'E')
chateau.ajouterArete('E', 'B')
chateau.ajouterArete('E', 'C')
chateau.ajouterArete('C', 'G')
chateau.ajouterArete('F', 'C')
chateau.ajouterArete('C', 'E')
chateau.ajouterArete('C', 'F')
chateau.afficher()

#Exercice 3


def parcoursProf1(g, s):
    assert s in g.sommets(), "le sommet est pas dans le graphe"
    rez = set(s)
    a_visiter = Pile()
    a_visiter.empiler(s)
    while not a_visiter.estVide():
        sommet = a_visiter.depiler()
        rez.add(sommet)
        for Vois in g.voisins(sommet):
            if not Vois in rez:
                a_visiter.empiler(Vois)
    return rez


print(parcoursProf1(chateau, "A"))


def existeChemin(g, s1, s2):
    return s2 in parcoursProf1(g, s1)


#Exercice 4
"""Programmez la fonction en utilisant les deux lignes de codes présentes"""


def parcoursProfRecurr(g, visites, s):
    """réalise le parcours en profondeur d'un graphe g à partir du sommet s et enregistre les sommets visités dans l'ensemble  visites"""

    if s not in visites:
        for individus in pla
        pass

    for vois in g.voisins(s):

        pass


#Exercice 5


#version itérative
def parcours_ch(g, s):

    pass


#version récursive
def parcours_ch(g, s):

    pass


def creerChemin(g, s1, s2):

    pass


#Exercice 6
"""Programmez le graphe de l'exercice"""


#q4
def chercheCycle_S(g, marques, s):

    pass


##Parcours BFS
#Exercice 7
"""Programmez la ou les fonctions nécéssaires pour réaliser le parcours en largeur d'un graphe"""
