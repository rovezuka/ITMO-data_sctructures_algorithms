'''A sequence of matrices A, B, C, ... , Z is given in such a way that 
it is possible to perform associative operations on them. Using 
dynamic programming, minimize the number 
of scalar operations to find their product.'''
from numpy import array, dot
M = [array([[1,2,3],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]]),
array([[1,2,3],[7,8,9],[7,8,9]]),
array([[1,2,3,4],[7,8,9,1],[10,11,12,3]]),
array([[1,2,4],[7,9,1],[10,12,3],[8,10,31]])]
for i in range(1,len(M)):
    M[i]=M[i-1].dot(M[i])
print('Результат умножения матриц:')
for i in range(len(M[-1])):
    for j in range(len(M[-1][i])):
        print(M[-1][i][j], end = ' ')
    print()
D = []
for i in range(len(M)):
    D.append([])
    for j in range(len(M)):
        D[i].append(float('inf'))
def MatrixMultTD(i,j):
    if D[i][j]==float('inf'):
        if i == j:
            D[i][j]=0
        else:
            for k in range(i,j):
                l = MatrixMultTD(i,k)
                r = MatrixMultTD(k+1,j)
                D[i][j]=min(D[i][j],l+r+len(M[i])*len(M[k][0])*len(M[j][0]))
    return D[i][j]
print('Минимальное количество скалярных операций для нахождения произведения:',MatrixMultTD(0,len(M)-1))