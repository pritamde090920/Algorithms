from collections import defaultdict

parent=[-1]*20


def dfs_tree(graph,s,visited):
    visited[s]=True
    print(s,end=" ")
    l=graph.get(s)
    for i in l:
        if visited[i]==False:
            parent[i]=s
            dfs_tree(graph,i,visited)

def add_edge(g,u,v):
    g[u].append(v)
    g[v].append(u)
    return g


v=int(input("Enter the number of vertices:"))
e=int(input("Enter the number of edges:"))
s=int(input("Enter the starting vertex:"))
graph=defaultdict(list)

print("Enter the edges:")
for i in range(e):
    x,y=input().split("-")
    x=int(x)
    y=int(y)
    graph=add_edge(graph,x,y)

visited=[False]*(v+1)

print("The dfs traversal:")
dfs_tree(graph,s,visited)
for i in range(0,v+1):
    if parent[i]!=-1:
        print(str(parent[i]),"-",str(i))
