from time import time

def testomatic(a, b): print( a == b )

##Création d'un tableau rempli avec le booleen False


def creerListe(n):
    return [[False] * n for _ in range(n)]

def print_matrice(mat):
  for a in mat: print(a)

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

"""
liste = liste_scrp(4)
liste[0][1] = liste[2][1] =liste[1][2]= liste[3][0] =liste[3][2] = True
print_matrice(liste)
"""

##Exercice 6 : Programmez les algorithmes demandé dans cet exercice


#6.1

def ordre(mat):
    return len(mat)

#ordre(liste)

#6.2

def degre(mat,s):
    return mat[s].count(True)

#print(degre(liste,0))

#6.3

def existeChemin(mat,a, b):
    return mat[a][b]

#print(existeChemin(liste,1,2))

##Exercice 7 et 8


class Graphe:
    """un graphe représenté par une matrice d'ajacence, où les sommets sont représentés par les entiers 0,1,...,n-1"""
    def __init__(self, n):
        self.ordre = n
        self.adj = [[False] * n for _ in range(n)]

    def printer(self):
      for a in self.adj: print (a)

    def ajouterArete(self, s1, s2):
        """crée l'arete orientée s1->s2"""
        assert s1<self.ordre and s2<self.ordre, "un sommet n'existe pas"
        self.adj[s1][s2] = True

    def arete(self, s1, s2):
        """teste si l'arete orientée s1->s2 existe"""
        assert s1 + s2 < 2*self.ordre, "un sommet n'existe pas"
        return self.adj[s1][s2]

    def voisins(self, s):
        """renvoie la liste des sommets voisins de s"""
        assert s<self.ordre, "ce sommet n'existe pas"
        liste = []
        for a in range(self.ordre):
            if self.arete(s,a): liste.append(a)
        return liste

    def afficher(self):
      _str_ = ""
      for a in range(self.ordre):
        str_=f"{a} ->"
        for b in range(self.ordre):
          if self.adj[a][b]:
            str_+= f" {b}"
        _str_ += str_ + "\n"
      return _str_

#Créer l'instance g =

g = Graphe(4)
test = Graphe(4)
"""
g.ajouterArete(0,1)
g.ajouterArete(0,3)
g.ajouterArete(1,2)
g.ajouterArete(3,1)
print(g.afficher())
"""

test.ajouterArete(0,1)
res1 = test.arete(0,1)
res1 = test.arete(0,2)

testomatic(True,res1)
testomatic(False,res1)
test.printer()
print(test.afficher())

##Exercice 9 : Programmez les méthodes de la classe Graphe2 ET 10



class Graphe2:
    """un graphe défini comme un disctionnaire d'adjacence"""
    def __init__(self, n):
        self.adj = {}

    def ajouterSommet(self, s):
        """ajoute au graphe un nouveau sommet s"""
        self.adj[s] = set()

    def ajouterArete(self, s1, s2):
        """crée l'arete orientée s1->s2, en créeant si besoin est le/s sommet/s manquant"""
        keys_ = set(keys_ for keys_ in self.adj)
        if not s1 in keys_ : self.ajouterSommet(s1)
        if not s2 in keys_ : self.ajouterSommet(s2)
        self.adj[s1].add(s2)

    def arete(self, s1, s2):
        """teste si l'arete orientée s1->s2 existe"""
        if s2 in self.adj[s1] : return True
        return False

    def sommets(self):
        """renvoie al liste des sommets qui composent le graphe"""
        return set(keys_ for keys_ in self.adj)

    def voisins(self, s):
        """renvoie la liste des sommets voisins de s"""
        return set(values for values in self.adj[s])

    def supprArete(self,s1,s2):
        """supprime l'arete de s1 -> s2"""
        self.adj[s1].discard(s2)

    def supprSommet(self,s):
        """supprime le sommet s du dictionnaire"""
        del(self.adj[s])

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""
        # pas demandé dans les consignes


graph_ = Graphe2('Nothing is True')
graph_.ajouterArete('A','B')
graph_.ajouterArete('A','C')
graph_.ajouterArete('C','A')
graph_.ajouterArete('B','A')
print(graph_.sommets())
print(graph_.voisins('A'))
graph_.supprArete('A','C')
print(graph_.adj)

##Exercice 11 : Coloriage !

