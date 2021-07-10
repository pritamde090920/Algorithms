from collections import defaultdict

parent=[-1]*20
connected=[]

def bfs(g,s,visited):
    queue=[]
    queue.append(s)
    visited[s]=True
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        connected.append(s)
        l=g.get(s)
        for i in l:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

def add_edge(g,u,v):
    g[u].append(v)
    g[v].append(u)
    return g

def shortest_path(g,start,goal):
    explored=[]
    queue=[[start]]
    if start==goal:
        print("Shortest path : ",start)
        return
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node not in explored:
            neighbours=g[node]
            for neighbour in neighbours:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour==goal:
                    print("Shortest path:",*new_path)
                    return
            explored.append(node)

v=int(input("Enter the number of vertices:"))
e=int(input("Enter the number of edges:"))
source=int(input("Enter the starting vertex:"))
graph=defaultdict(list)

d=dict()
print("Enter the edges:")
for i in range(e):
    x,y=input().split("-")
    x=int(x)
    y=int(y)
    graph=add_edge(graph,x,y)
    t=d.get(x,[])
    t.append(y)
    d[x]=t
    t=d.get(y,[])
    t.append(x)
    d[y]=t

visited=[False]*(v+1)

print("\nThe bfs traversal:")
p=''
bfs(graph,source,visited)
for i in range(0,v+1):
    if parent[i]!=-1:
        print(str(parent[i]),"-",str(i))

print()
print("\nNumber of connected componenets is:",len(connected)-v+1)
if(len(connected)==v):
    print("Connected graph!")
else:
    print("Not connected graph!")

print()
while(1):
    dest=int(input("Enter destination vertex(-1 to exit):"))
    if dest==-1:
        break
    else:
        shortest_path(graph,source,dest)
