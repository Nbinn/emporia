from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list) # A list of lists to represent a graph

    # add edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    #number of place to travel
    def length(self):
        return len(self.graph)
    #find ways to traverse the without missing any place and each empty place is only visited once.
    def findRoute(self,graph,source,des,path,visited):
        # the number of the way can travel from source to destination, not missing any empty place
        global count
        if(source == des):
            # if the way travel from source to destination not missing any empty place
            if(len(path) == graph.length()):
                count += 1
            return
        # Check if every way starting from cell start leads to a solution or not
        for w in self.graph[source]:
            # path visit each place exactly once
            if visited[w-1] == False:
                visited[w-1] = True
                path.append(w)
                # check if adding cell w to the way leads to the solution or not
                graph.findRoute(graph,w,des,path,visited)
                #backtrack
                visited[w-1] = False
                path.pop()
# check cell
def isSafe(i, j, matrix):
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
        if(matrix[i][j] != 0 and matrix[i][j] != 1 and matrix[i][j] != 2 and matrix[i][j] != 3):
            print("error in cell:",i,j)
            return False
        else:
            return True
    else:
        return False

def findPath(matrix,m ,n):
    global count
    count = 0
    source, des = None, None # place to start and finish
    countSrc,countDes = 0, 0
    graph = Graph() #create graph
    place = 1 # number of current place
    for i in range(m):
        for j in range(n):
            if(matrix[i][j] != 1):
                # connect all adjacent place to current place if can move
                if (isSafe(i, j + 1, matrix)):
                    if(matrix[i][j+1] != 1):
                        graph.addEdge(place, place + 1)
                if (isSafe(i, j - 1, matrix)):
                    if (matrix[i][j - 1] != 1):
                        graph.addEdge(place, place - 1)
                if (isSafe(i + 1, j, matrix)):
                    if (matrix[i+1][j] != 1):
                        graph.addEdge(place, place + n)
                if (isSafe(i - 1, j, matrix)):
                    if (matrix[i-1][j] != 1):
                        graph.addEdge(place, place - n)
            # source index
            if (matrix[i][j] == 2):
                source = place
                countSrc += 1
            # destination index
            if (matrix[i][j] == 3):
                des = place
                countDes += 1
            place += 1
    if(source == None):
        print("error: There is no start place")
        return
    if(des == None):
        print("error: There is no end place")
        return
    if(countSrc > 1):
        print("error: There are too many start place")
        return
    if(countDes > 1):
        print("error: There are too many end place")
        return
    #add the start place to path
    path = []
    path.append(source)
    #mark the start place is visited
    visited = [False] * (m*n)
    visited[source-1] = True
    #calculate all the possible way
    graph.findRoute(graph,source,des,path,visited)
    print(count)

# input from stdin
# the number of rows and columns
m, n = input().split()
#
matrix = []
for i in range(int(m)):
    data = input().split()
    #check input has exactly n digits
    while(len(data) != int(n)):
        print("error")
        data = input().split()

    data = [int(i) for i in data]
    matrix.append(data)

findPath(matrix,int(m),int(n))
