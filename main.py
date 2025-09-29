#### Fonctions secondaires

# imports
"""module providing the graph of the syracuse series"""
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """la fonction produit le graphe"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """\
        retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n"""
    l = [ ]
    uk=n
    while uk>1:
        if uk%2==0:
            uk=uk//2
            print(uk)
            l.append(uk)
            print(l)
        else:
            uk=uk*3+1
            l.append(uk)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol"""
    # votre code ici
    n = 0
    for  inner_l, l in enumerate(l): #parcourir la liste afin d'avoir le temps de vol de la suite
        n+=inner_l

    return n-1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    # votre code ici
    n = l[0]
    for i, valeur in enumerate(l):
        if valeur<=n and i>0:
            return i
    return len(l)-1
def altitude_maximale(l):
    """\
        retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale"""
    # votre code ici
    return max(l) #voir le max de la liste qui correspond à l'altitude_maximale
#### Fonction principale
def main():
    """ vos appels à la fonction secondaire ici"""
    n=20
    lsyr = syracuse_l(n)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))
    print("chaîne test")
if __name__ == "__main__":
    main()
    #End-of-file (EOF)
