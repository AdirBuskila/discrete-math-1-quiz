import networkx as nx
E="ab bc cd de ea af bg ch di ej fh hj jg gi if".split()
G=nx.Graph([(e[0],e[1]) for e in E]); H=nx.complement(G)
print(G.number_of_edges(),set(dict(G.degree).values()),nx.diameter(G),nx.is_isomorphic(nx.petersen_graph(),G))
print('Hdeg',set(dict(H.degree).values()),'bip',nx.is_bipartite(H),'iso',nx.is_isomorphic(G,H),'connected',nx.is_connected(H))
# hamilton
import itertools
vs=list(H); 
def ham(H):
    s=vs[0]
    def rec(p,seen):
        if len(p)==len(vs): return H.has_edge(p[-1],s)
        return any(rec(p+[w],seen|{w}) for w in H[p[-1]] if w not in seen)
    return rec([s],{s})
print('ham',ham(H),'G ham',ham(G))
