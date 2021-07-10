capacity=int(input("Enter the capacity of the knapsack:"))
weight=list(map(int,input("Enter the weights(seperated by a space) of the items:").split()))
value=list(map(int,input("Enter the values(seperated by a space) of the items:").split()))
cur_weight,profit=0,0
greedy=[]
for i in range(len(weight)):
    greedy.append(value[i]/weight[i])
while(cur_weight<capacity):
    val=max(greedy)
    ind=greedy.index(val)
    w,v=weight[ind],value[ind]
    if (cur_weight+w)<=capacity:
        cur_weight+=w
        profit+=v
        print("Added item of value "+str(v)+" and weight "+str(w)+" completely into the knapsack. space left :"+str(capacity-cur_weight))
    else:
        rem_weight=capacity-cur_weight
        frac=rem_weight/w
        cur_weight+=(w*frac)
        profit+=(v*frac)
        print("Added "+format(frac,".4f")+" fraction of the item of value "+str(v)+" and weight "+str(w)+" into the knapsack. space left :"+str(capacity-cur_weight))
    value.remove(v)
    greedy.remove(val)
    weight.remove(w)
print("The maximum profit of the knapsack is:",profit)
