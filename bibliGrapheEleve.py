class Grapheprout:
    """un graphe défini comme un dictionnaire d'adjacence"""

    def __init__(self):
        """constructeur avec l'attribut adj qui permet de stocker le dictionnaire"""

        self.adj = {}

    def ajouterSommet(self,s):
        """ajoute au graphe un nouveau sommet s"""
        self.adj[s]=set()

    def ajouterArc(self,s1,s2):
        """crée l'arete orientée s1->s2, en créant si besoin est le/s sommet/s manquant"""
        if s1 not in self.adj:
            self.adj[s1] = set()
        if s2 not in self.adj:
            self.adj[s2] = set()
        self.adj[s1].add(s2)

    def ajouterArete(self,s1,s2):
        """crée l'arete non orientée s1<->s2, en créant si besoin est le/s sommet/s manquant"""
        if s1 not in self.adj:
            self.adj[s1] = set()
        if s2 not in self.adj:
            self.adj[s2] = set()
        self.adj[s1].add(s2)
        self.adj[s2].add(s1)

    def arete(self,s1,s2):
        """teste si l'arete orientée s1->s2 existe"""

        return s1 in self.adj and s2 in self.adj[s1]

    def sommets(self):
        """renvoie la liste des sommets qui composent le graphe"""
        res = []
        for s in self.adj:
            res.append(s)
        return res

    def voisins(self,s):
        """renvoie la liste des sommets voisins de s"""
        res = []
        for v in self.adj[s]:
            res.append(v)
        return res

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""
        for s in self.adj:
            vois = ''
            for v in self.adj[s]:
                vois = vois+' '+str(v)
            print(str(s)+'->'+vois)

    def suprArete(self,s1,s2):
        if s1 in self.adj:
            self.adj[s1].discard(s2)

    def supprSommet(self,s1):
        if s1 in self.adj:
            del self.adj[s1]
            for s in self.adj:
                self.adj[s].discard(s1)

    def degre(self,s):
        res = 0
        if s not in self.adj:
            return None
        for val in self.adj[s]:
            res+=1
        return res

    def ordre(self):
        res = 0
        for s in self.adj:
            res+=1
        return res


class GrapheP:
    """un graphe défini comme un disctionnaire d'adjacence"""

    def __init__(self):

        self.adj = {}

    def ajouterSommet(self,s):
        """ajoute au graphe un nouveau sommet s"""
        self.adj[s]={}

    def ajouterArc(self,s1,s2,p):
        """crée l'arete orientée s1->s2, en créeant si besoin est le/s sommet/s manquant avec la podération p"""
        if s1 not in self.adj:
            self.adj[s1] = {}
        if s2 not in self.adj:
            self.adj[s2] = {}
        self.adj[s1][s2]=p

    def ajouterArete(self,s1,s2,p):
        """crée l'arete non orientée s1<->s2, en créeant si besoin est le/s sommet/s manquant"""
        if s1 not in self.adj:
            self.adj[s1] = {}
        if s2 not in self.adj:
            self.adj[s2] = {}
        self.adj[s1][s2]=p
        self.adj[s2][s1]=p

    def arete(self,s1,s2):
        """teste si l'arete orientée s1->s2 existe"""

        return s1 in self.adj and s2 in self.adj[s1]

    def sommets(self):
        """renvoie la liste des sommets qui composent le graphe"""
        res = []
        for s in self.adj:
            res.append(s)
        return res

    def voisins(self,s):
        """renvoie la liste des sommets voisins de s"""
        res = []
        for v in self.adj[s]:
            res.append(v)
        return res

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""
        for s in self.adj:
            vois = ''
            for v in self.adj[s]:
                vois = vois+' '+str(v)
            print(str(s)+'->'+vois)

    def suprArete(self,s1,s2):
        if s1 in self.adj:
            del self.adj[s1][s2]

    def supprSommet(self,s1):
        if s1 in self.adj:
            del self.adj[s1]
            for s in self.adj:
                del self.adj[s][s1]

    def degre(self,s):
        res = 0
        if s not in self.adj:
            return None
        for val in self.adj[s]:
            res+=1
        return res

    def ordre(self):
        res = 0
        for s in self.adj:
            res+=1
        return res
##Pile

class Cellule:
    """ définit la classe Cellule"""
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)

##

class Pile:
    def __init__(self):
        self.contenu = None

    def empiler(self,x):

        self.contenu = Cellule(x,self.contenu)

    def estVide(self):
        return self.contenu is None

    def __str__(self):

        res = ''
        l = self.contenu
        while not l is None:
            res = res + str(l.valeur) + ' '
            l = l.suivante

        return res

    def depiler(self):

        if self.contenu is None:
            raise IndexError("Vous dépilez une liste vide !")

        val = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return val

class File:

    def __init__(self):

        self.tete = None
        self.queue = None

    def estVide(self):
        return self.tete is None

    def enfiler(self,x):

        c = Cellule(x,None)

        if self.tete is None:
            self.tete = c

        else:
            self.queue.suivante = c

        self.queue = c

    def __str__(self):

        if self.tete is None:
            res = ''
        else :
            res = ''
            l = self.tete
            while not l is None:
                res = res + str(l.valeur) + ' '
                l = l.suivante
            l1 = self.queue
            res= res+'|'
            while not l1 is None:
                res = res + str(l1.valeur)+' '
                l1 = l1.suivante
            #res = res+'|'+ str(self.queue.valeur)
        return res

    def defiler(self):
        if self.tete is None:
            raise IndexError("Attention File vide !")
        val = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return val