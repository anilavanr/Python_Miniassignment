def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


# Driver Code
list1 = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
print(Repeat(list1))