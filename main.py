from time import time

##Création d'un tableau rempli avec le booleen False


def creerListe(n):
    return [[False] * n for _ in range(n)]


#Question 1 : Expliquez comment, avec les instructions données, le tableau a pu se créer ainsi

#Question 2 : Ecrire un algorithme sans utiliser les listes par compréhension


def liste_scrp(n):

    liste = []

    for a in range(n):

        liste2 = []

        for prout in range(n):

            liste2.append(False)

        liste.append(liste2)

    return liste


liste = liste_scrp(3)
liste[0]

##Exercice 6 : Programmez les algorithmes demandé dans cet exercice


#6.1
def ordre(mat):
    return len(mat)

ordre(liste)

#6.2

def degre(s):
    return s.count(True)

degre()

#6.3


def existeChemin(a, b):

    pass


##Exercice 7 et 8


class Graphe:
    """un graphe représenté par une matrice d'ajacence, où les sommets sont représentés par les entiers 0,1,...,n-1"""
    def __init__(self, n):
        self.ordre = n
        self.adj = [[False] * n for _ in range(n)]

    def ajouterArete(self, s1, s2):
        """crée l'arete orientée s1->s2"""

    def arete(self, s1, s2):
        """teste si l'arete orientée s1->s2 existe"""

    def voisins(self, s):
        """renvoie la liste des sommets voisins de s"""

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""


#Créer l'instance g =

##Exercice 9 : Programmez les méthodes de la classe Graphe2


class Graphe2:
    """un graphe défini comme un disctionnaire d'adjacence"""
    def __init__(self, n):

        self.adj = {}

    def ajouterSommet(self, s):
        """ajoute au graphe un nouveau sommet s"""

    def ajouterArete(self, s1, s2):
        """crée l'arete orientée s1->s2, en créeant si besoin est le/s sommet/s manquant"""

    def arete(self, s1, s2):
        """teste si l'arete orientée s1->s2 existe"""

    def sommets(self):
        """renvoie al liste des sommets qui composent le graphe"""

    def voisins(self, s):
        """renvoie la liste des sommets voisins de s"""

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""
