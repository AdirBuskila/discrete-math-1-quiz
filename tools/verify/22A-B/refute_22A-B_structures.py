import networkx as nx, itertools
E=[('a','b'),('a','e'),('a','f'),('b','c'),('b','g'),('c','d'),('c','h'),('d','e'),('d','i'),('e','j'),('f','i'),('f','h'),('g','j'),('g','i'),('h','j')]
G=nx.Graph(E); C=nx.complement(G)
print(len(G.edges),sorted(dict(G.degree).values()),nx.diameter(G),nx.is_bipartite(C),nx.is_connected(C),set(dict(C.degree).values()))
# hamilton brute
nodes=list(C.nodes);ham=False
def dfs(path,seen):
    global ham
    if ham:return
    if len(path)==10:
        ham = C.has_edge(path[-1],path[0]);return
    for v in C[path[-1]]:
        if v not in seen: dfs(path+[v],seen|{v})
dfs(['a'],{'a'}); print('ham',ham, 'triangle adg',C.has_edge('a','d'),C.has_edge('d','g'),C.has_edge('a','g'))
for t in [('a','b','c'),('a','e','f'),('d','i','c')]: print(t,all(C.has_edge(x,y) for x,y in itertools.combinations(t,2)))
for n in range(2,13):
    P=nx.path_graph(n);Cc=nx.complement(P)
    print(n,nx.is_connected(Cc),nx.is_bipartite(Cc),end='; ')
print()
# 23A-B 1b/2b/etc: euclid
from sympy import gcdex
print(gcdex(55,-40),gcdex(55,40),gcdex(68,84),gcdex(84,68))
# 22A-B 3b counts
f=lambda k:(k*k)%6+2
from collections import defaultdict
d=defaultdict(list)
for k in range(1,8):d[f(k)].append(k)
print(dict(d))
# 23A-B 2c: total orders on {1,2}
import itertools
pairs=[(i,j) for i in (1,2) for j in (1,2)]
def tot(R):
    return all((x,x) in R for x in (1,2)) and all(not((x,y) in R and (y,x) in R) or x==y for x,y in pairs) and all(((x,y) in R or (y,x) in R) for x,y in pairs) and all(((x,z) in R) for (x,y) in R for (y2,z) in R if y==y2)
ords=[set(s) for r in range(5) for s in itertools.combinations(pairs,r) if tot(set(s))]
print(ords)
# 3b: card of 5^m 9^n
A={5**m*9**n for m in range(10) for n in range(10)};B={5**m*7**n for m in range(10) for n in range(10)}
print(len(A),len(B),len(A&B),len(A|B))
A={3**n*5**m for m in range(20) for n in range(20)};B={2**n*5**m for m in range(20) for n in range(20)}
print(len(A&B),len(A-B))
A={3**n*7**m for m in range(30) for n in range(30)};B={3**n*5**m for m in range(30) for n in range(30)}
print(len(A&B),len(A-B))
A={3**n*5**m for m in range(11) for n in range(11)};B={5**m for m in range(1,11)};print(len(A-B),len(A|B),B<=A)
B={3**n for n in range(1,11)};print(len(A-B),len(A|B),B<=A)
