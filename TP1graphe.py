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
        if not s1 in keys_: self.ajouterSommet(s1)
        if not s2 in keys_: self.ajouterSommet(s2)
        self.adj[s1].add(s2)

    def lier(self, s1, s2):
        self.ajouterArete(s1, s2)
        self.ajouterArete(s2, s1)

    def arete(self, s1, s2):
        """teste si l'arete orientée s1->s2 existe"""
        if s2 in self.adj[s1]: return True
        return False

    def sommets(self):
        """renvoie al liste des sommets qui composent le graphe"""
        return set(keys_ for keys_ in self.adj)

    def voisins(self, s):
        """renvoie la liste des sommets voisins de s"""
        return self.adj[s]

    def supprArete(self, s1, s2):
        """supprime l'arete de s1 -> s2"""
        self.adj[s1].discard(s2)

    def supprSommet(self, s):
        """supprime le sommet s du dictionnaire"""
        del (self.adj[s])

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""

        for a in list(self.adj.items()):
            print(a)


graph_ = Graphe2('Nothing is True')

graph_.lier('A', 'B')
graph_.lier('C', 'B')
graph_.lier('A', 'C')
graph_.lier('A', 'D')
graph_.lier('D', 'B')
graph_.lier('D', 'E')
graph_.lier('B', 'E')
graph_.lier('C', 'E')
#graph_.afficher()


##Exercice 11 : Coloriage !

def voisin_here(voisins, listecoul):
    """revoie le bouleen correspondant à l'appartenance du set voisin dans le set correspondant au set liste coul"""
    for sommet_voisin in voisins:
        if sommet_voisin in listecoul: return True
    return False


def coloriage(graph):
    """renvoie le dictionnaire des couleurs associés aux sommet et le nombre de couleurs"""
    nbr_coul = 1
    dico_rez = [set()]

    for sommet in graph.adj:
        voisins = graph.voisins(sommet)
        for num_coul in range(nbr_coul):
            if not voisin_here(voisins, dico_rez[num_coul]):
                dico_rez[num_coul].add(sommet)
                break
        else:
            dico_rez.append(set(sommet))
            nbr_coul += 1
    return dico_rez, nbr_coul

print(coloriage(graph_))