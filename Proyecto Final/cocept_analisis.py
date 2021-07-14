#Order
#origin : {destination1 : time, destination2 : time, destination3 : time}
#if l not in (dic.get(l) if dic.get(l) != None else []) if l != x

from graphviz import Graph, Digraph
import random as rd

def random_generate_edge(n):
    dic = {}
    for x in n:
        for y in n[rd.randint(0,len(n)):rd.randint(0,len(n))]:
            if dic.get(x) == None:
                dic[x] = {}
            if y not in (dic.get(x) if dic.get(x) != None else {}).keys() and x != y:
                dic[x][y] = rd.randint(1,10)
                if dic.get(y) == None:
                    dic[y] = {}
                dic[y][x] = dic[x][y] 
    return dic

#Opcion 1: FOR FOR
def for_for(origin, destination, graph, log = []):
    if destination in graph[origin]:
        return log + [destination]
    cont = []
    for x in graph[origin].keys():
        cont.append(for_for(x, destination, graph,log = log + [x]))
        print(cont)
    return sorted(cont, key = len)[0]

#ex = random_generate_edge(['A','B','C','D','E','F','G','H'])
#print(ex)
origin = 'A'
destination = 'E'
#print(for_for(origin, destination, ex))
# OPCION Terrible O(n^n), even acounting for no usage of comparators of distance
#Opcion 2: Dijkstra's algorithm
 #Using recursion, the shortest path is created
 #May need to modify as only finds value of shortest path

#ex = {'E': {'D': 6, 'F': 5}, 'D': {'E': 6, 'F': 9}, 'F': {'C': 4, 'D': 9, 'E': 5, 'G': 6, 'H': 6}, 'C': {'F': 4}, 'G': {'F': 6}, 'H': {'F': 6}}

# Basic outline https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

def dijkstra(origin, destination, graph, log = [], first = True):
    if first:
        log = {x: float('inf') for x in graph.keys()} # 1.Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
        log[origin] = 0 # 2.Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
    # 5. If the destination node has been marked visited 
    # (when planning a route between two specific nodes) or 
    # if the smallest tentative distance among the nodes in the 
    # unvisited set is infinity (when planning a complete traversal; 
    # occurs when there is no connection between the initial node and remaining unvisited nodes), 
    # then stop. The algorithm has finished.
    if destination in graph[origin]:
        return log[origin] + graph[origin][destination]
    # 3. For the current node, consider all of its unvisited neighbours and calculate their 
    # tentative distances through the current node. Compare the newly calculated tentative 
    # distance to the current assigned value and assign the smaller one. For example, 
    # if the current node A is marked with a distance of 6, and the edge connecting 
    # it with a neighbour B has length 2, then the distance to B through A will be 6 + 2 = 8. 
    # If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
    for x in graph[origin]:
        if x in log.keys():
            log[x] = min(log[origin] + graph[origin][x], graph[origin][x])
    # 4. When we are done considering all of the unvisited neighbours
    # of the current node, mark the current node as visited and 
    # remove it from the unvisited set. A visited node will never be checked again.
    log.pop(origin)
    new_origin = min(log)
    if log.get(new_origin) == None:
        return None
    # 6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
    # set it as the new "current node", and go back to step 3.
    return dijkstra(new_origin, destination, graph, log=log, first = False)

#print(dijkstra(origin, destination, ex))

#pt, mod for our purposes

def dijkstra(origin, destination, graph, log = [], first = True):
    if first:
        log = {x: [float('inf'),[]] for x in graph.keys()} # Now contains extra information
        if not(origin in log):
          return None, None
        log[origin][0] = 0
    if destination in graph[origin]:
        log[destination][0] = log[origin][0] + graph[origin][destination]
        log[destination][1] = log[origin][1] + [origin] + [destination]
        return log
    for x in graph[origin]:
        if x in log.keys(): # Modded to work with new changes
            if log[origin][0] + graph[origin][x] <= log[x][0]:
                log[x][0] = log[origin][0] + graph[origin][x]
                log[x][1] = log[origin][1] + [origin]
            elif log[origin][0] + graph[origin][x] > log[x][0]:
                pass
    log.pop(origin)
    new_origin = min(log, key= lambda x: log[x][0], default = None)
    if log.get(new_origin) == None:
        return None
    return dijkstra(new_origin, destination, graph, log = log, first = False)

#path = dijkstra(origin, destination, ex)[destination][1]

#Needs work
def nodifing(dic):
  out = dic.copy()
  for x in dic.keys():
    for y in dic[x].keys():
      if dic.get(y) == None:
        out[y] = {}
      out[y][x] = out[x][y]
  return out


"""
sum = 0
current = ex[origin]
path = path [1:] + [destination]
for x in path:
    sum  += current[x]
    current = ex[x]
print(sum)
"""

# Once generated the grafix, this with output
# the shortest path via the algoritm
# Lets test this out

ex = random_generate_edge(['A','B','C','D','E','F','G','H'])
if origin not in ex and destination not in ex:
  ex = random_generate_edge(['A','B','C','D','E','F','G','H'])

print({x: {} for x in ['A','B','C','D','E','F']})
ex = {'A':{'B':7, 'C':9, 'F':14}, 'F':{'E':9}, 'D':{'B':15, 'E':6}}
#WIKI EXAMPLE
ex = {'A': {'B':7, 'C':9, 'F':14}, 'B': {'A':7, 'D':15 }, 'C': {'B':10, 'A':9, 'F':2, 'D':11}, 'D': {'B':15, 'C':11, 'E' : 6}, 'E': {'D' : 6, 'C':11, 'B':15}, 'F': {'A':14, 'C':2, 'E':9}}
print(ex)
input()
origin = 'A'
destination = 'E'

g = Graph(strict=True)

for x in ex.keys():
  for y in ex[x]:
    g.edge(x, y, label = str(ex[x][y]))

distance, path = dijkstra(origin, destination, ex)[destination]

print(ex)
print(path)
print(f"Origen = {origin}, Destino = {destination}")
print(f"Distancia: {distance}")

for x in range(len(path)-1):
  g.edge(path[x], path[x+1],color='red')

g