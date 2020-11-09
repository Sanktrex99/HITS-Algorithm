import numpy as np
import math

class Graph(object):

    # Initialize the matrix
    def _init_(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1           
#graph input 
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)


# Hyperlink Induced Topic Search Given Adjacency Matrix 
def hits(A):
    hubVectorLst = []
    transpose = np.transpose(A)
    n = len(A[0]) 
    for i in range(n):
        hubVectorLst.append(1)
    hubVector = np.array(hubVectorLst)
    authorityVector = np.dot(transpose, hubVector)
    hubVector = np.dot(A, authorityVector)
    print("Hub Vector: ", hubVector)
    print("Authority Vector: ", authorityVector)

print("HITS Algorithm on ", g.adjMatrix)
hits(g.adjMatrix)
