def transpose(matrix):
    nuevaMat=[]
    
    for n in range(len(matrix[0])):
        nuevaMat.append([])
        for k in range(len(matrix)):
            nuevaMat[n].append(matrix[k][n])
    return nuevaMat
    pass
