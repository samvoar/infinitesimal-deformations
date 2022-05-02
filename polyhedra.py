import numpy as np
from numpy.linalg import matrix_rank

# v and w are adjacent vertices, l -- matrix of realized edges

#incidence matrices of a minimal triangulation of a torus with two faces removed
#and of a star with 8 faces.

torus=np.array([[0,1,1,1,0,0,1],[1,0,1,0,0,0,1],[0,1,0,1,5,0,1],[1,0,1,0,1,1,1],
[1,0,1,1,0,1,1],[0,0,0,1,1,0,1],[1,1,1,1,1,1,0]],dtype=object)

star=np.array([[0,1,0,0,0,0,0,1,1],
[1,0,1,0,0,0,0,0,1],
[0,1,0,1,0,0,0,0,1],
[0,0,1,0,1,0,0,0,1],
[0,0,0,1,0,1,0,0,1],
[0,0,0,0,1,0,1,0,1],
[0,0,0,0,0,1,0,1,1],
[1,0,0,0,0,0,1,0,0],
[1,1,1,1,1,1,1,1,0]],dtype=object)


def random(n):  #generate random embedding of n points
    np.random.seed(341)
    randnums=np.zeros(n,dtype=object)
    for i in range(0,n):
          randnums[i]=np.random.randint(-10,100, size=3)
    return randnums


def makematrix(l,n):   #make a system of linear equations from the matrix of vector realization l
    v=0
    w=0
    A=np.zeros(3*n)
    for v in range(0, n):
        for w in range(0, n):
            if  np.any(l[w][v]!=0):
                newrow = np.zeros(3*n)
                newrow[v] = l[w][v][0]
                newrow[n+v] = l[w][v][1]
                newrow[2*n+v] = l[w][v][2]
                newrow[w] = -l[w][v][0]
                newrow[n+w] = -l[w][v][1]
                newrow[2*n+w] = -l[w][v][2]
                A = np.vstack((A, newrow))
    A = np.delete(A, (0), axis=0)
    return A


def graphrealiz(graph,coord,n):   #turn incidence matrix and embedding of n vetices into a matrix of vector realization of edges
    for i in range(0,n):
         for j in range(0,n):
            if graph[i][j]!=0:
                graph[i][j]=coord[i]-coord[j]
    return graph


n=9
print("The dimension at the random embedding of a star with {} triangles is".format(n))
print(3*n-matrix_rank(makematrix(graphrealiz(star,random(n),n),n))-6)

n=7
print("The dimension at the random embedding of a minimal triangulation of the torus with two triangles removed is")
print(3*n-matrix_rank(makematrix(graphrealiz(torus,random(n),n),n))-6)
