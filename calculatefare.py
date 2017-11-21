graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
       [4, 0, 8, 0, 0, 0, 0, 11, 0],
       [0, 8, 0, 7, 0, 4, 0, 0, 2],
       [0, 0, 7, 0, 9, 14, 0, 0, 0],
       [0, 0, 0, 9, 0, 10, 0, 0, 0],
       [0, 0, 4, 14, 10, 0, 2, 0, 0],
       [0, 0, 0, 0, 0, 2, 0, 1, 6],
       [8, 11, 0, 0, 0, 0, 1, 0, 7],
       [0, 0, 2, 0, 0, 0, 6, 7, 0]
       ]
def minDistance(dist, sptSet):

    min = 1000

    for v in range(9):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def printSolution(dist,V,des):
    for node in range(V):
        if node==des:
            return dist[node]

def djikstra(src,des):

    dist=[1000]*9
    sptSet=[False]*9

    dist[src]=0

    for i in range(8):
        u=minDistance(dist,sptSet)
        sptSet[u]=True

        for v in range(9):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return printSolution(dist,9,des)

def find_distance(source,dest):

    places={"Perambur":0 , "Anna Nagar":1 , "Padi":2 , "Vadapalani":3 , "Surapet":4 , "Mount Road":5, "Mylapore":6 , "Adyar":7 , "T Nagar":8 }
    src=places[source]
    des=places[dest]
    return djikstra(src,des)

def calculate_fare(src,dest,cabtype):
    cabs={"mini":12, "sedan":15 ,"suv":18}

    return cabs[cabtype]*find_distance(src,dest)
