def prims(n, edges, start):
    
    #Parsing
    dic = {}
    for i in range(len(edges)):
        if(edges[i][0] not in dic):
            dic[edges[i][0]] = [[edges[i][1],edges[i][2]]]
        else:
            dic[edges[i][0]].append([edges[i][1],edges[i][2]])
            
        if(edges[i][1] not in dic):
            dic[edges[i][1]] = [[edges[i][0],edges[i][2]]]
        else:
            dic[edges[i][1]].append([edges[i][0],edges[i][2]])
    
    #Algo Prim
    tree = set()
    tree.add(start)
    cost = 0
    
    for i in range(n-1):
        
        edge = None
        mini = math.inf
        
        
        for u in tree:
            tab = dic[u]
            
            for t in tab:
                if t[0] in tree:
                    continue
                
                if mini > t[1]:
                    mini = t[1]
                    edge = t[0]
                    
        cost += mini
        tree.add(edge)
        
    return(cost)
