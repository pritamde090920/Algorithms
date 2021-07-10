INF=9999999  
g=[]
for i in range(5):
    print("Enter the elements of row",i+1," of the adjacency matrix:")
    l=list(map(int,input().split()))
    g.append(l)
V=5
selected=[0, 0, 0, 0, 0]
no_edge=0
selected[0]=True
print("The minimal spanning tree is:")
print("Edge \tWeight")
while (no_edge<V-1):
    minimum=INF
    x=0
    y=0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and g[i][j]):  
                    if minimum>g[i][j]:
                        minimum=g[i][j]
                        x=i
                        y=j
    print(str(x)+" - "+str(y)+" \t"+str(g[x][y]))
    selected[y]=True
    no_edge+=1
