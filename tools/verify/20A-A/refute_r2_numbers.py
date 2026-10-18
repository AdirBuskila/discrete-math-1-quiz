import itertools, math, sympy as sp, networkx as nx
from itertools import combinations, product
# 1a
print('1a',sum(1 for c in combinations(range(1,10),4) if 1 in c and 2 in c))
# 1c: complement of K_mn bipartite
res=[]
for m in range(1,8):
  for n in range(1,8):
    G=nx.complete_bipartite_graph(m,n); H=nx.complement(G)
    if nx.is_bipartite(H): res.append((m,n))
print('1c',res)
# 3c complement of P_n
for n in range(1,14):
    P=nx.path_graph(n); H=nx.complement(P)
    odd=sum(1 for v in H if H.degree(v)%2)
    conn=nx.is_connected(H)
    edges=H.number_of_edges()
    # connected ignoring isolated
    nz=H.subgraph([v for v in H if H.degree(v)>0])
    c2=len(nz)==0 or nx.is_connected(nz)
    print('3c',n,'edges',edges,'odd',odd,'conn',conn,'conn_noniso',c2,'trail(strict conn)',conn and odd in(0,2),'trail(edges only)',c2 and odd in (0,2),'circuit',conn and odd==0)
# 4b
N=6;K=4
f=list(product(range(1,K+1),repeat=N))
print('4b nondecr',sum(all(a<=b for a,b in zip(x,x[1:])) for x in f),'strict',sum(all(a<b for a,b in zip(x,x[1:])) for x in f),'onto',sum(len(set(x))==K for x in f))
print(math.comb(9,3)) 
# 5a
def graphical(seq):
    s=sorted(seq,reverse=True)
    if sum(s)%2: return False
    n=len(s)
    for k in range(1,n+1):
        if sum(s[:k])>k*(k-1)+sum(min(x,k) for x in s[k:]): return False
    return True
print('5a',graphical([1,1,3,3,3,6,7,8]), 'max deg 8 on 8 vertices>7')
# 5b
cnt=0
for a in range(3,23):
 for b in range(1,23):
  for c in range(4,23):
   d=22-a-b-c
   if d>=2: cnt+=1
print('5b',cnt,math.comb(15,3))
# 6a
n=sp.symbols('n',positive=True,integer=True)
for nn in range(0,5):
    a=sum(math.comb(nn,k)*3**k*5**(nn-k) for k in range(nn+1)); b=sum(math.comb(nn,k)*7**k*5**(nn-k) for k in range(nn+1))
    print('6a',nn,a,b,sp.totient(a*b), 2**(5*nn)*3**(nn-1) if nn>=1 else None)
# 2c
print('2c phi(1)=phi(2)',sp.totient(1),sp.totient(2), all(sp.totient(n)%8==0 for n in range(15,3000,15)))
