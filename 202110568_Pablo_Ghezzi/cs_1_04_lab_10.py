#Semana_10
from graphviz import Graph

class node():
    def __init__(self, value, connected_nodes = []):
        self.value = value
        self.connected_nodes = connected_nodes
    def add_connection(self, node):
        self.connected_nodes.append(node)
        return None

node(10, [node(2),node(7)])

g = Graph()

g.edge('US','Peru')
g.edge('Peru','Bolivia')
g.edge('Bolivia','US')
g.render(directory='202110568_Pablo_Ghezzi/test.gv')

h = Graph()
g.render(directory='202110568_Pablo_Ghezzi/MiniPC')
while True:
    inp = input("Ingrese paises")

