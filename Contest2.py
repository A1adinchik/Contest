'''

Задача №1. От матрицы смежности к списку ребер, ориентированный вариант

n = int(input())
array = [[int(j) for j in input().split()] for i in range(n)]

def main(n, array):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                print(i+1, j+1)

main(n, array)
'''


'''

Задача №3. Полный граф

n, m = map(int, input().split())
array = [[int(j) for j in input().split()] for i in range(m)]

def create_adjacency_matrix(array, n, m):
    array_s = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        array_s[array[i][0]-1][array[i][1]-1] = array_s[array[i][0]-1][array[i][1]-1] = 1
    return array_s

def main(array_s, n, m):
    check_on_full = 1
    for i in range(n):
        for j in range(i+1, n, 1):
            if array_s[i][j] == 0:
                check_on_full = 0
    if check_on_full == 1:
        print("YES")
    else:
        print("NO")
        
array_s = create_adjacency_matrix(array, n, m)
main(array_s, n, m)
'''

'''

Задача №4. Транзитивность ориентированного графа

n = int(input())
array = [[int(j) for j in input().split()] for i in range(n)]

def main(arr, n):
    check_for_transitivity = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] and check_for_transitivity != 1:
                for z in range(n):
                    if (array[j][z] and not(array[i][z])):
                        print("NO")
                        check_for_transitivity = 1
    if check_for_transitivity == 0:
        print("YES")

main(array, n)
'''

'''

Задача №2. Полустепини вершин по спискам рёбер

n, m = map(int, input().split())
array = [[int(j) for j in input().split()] for i in range(m)]

def main(array, n, m):
    array_s = [[0 for j in range(2)] for i in range(n)]
    
    for i in range(m):
        array_s[array[i][1]-1][0]+=1
        array_s[array[i][0]-1][1]+=1

    for i in range(n):
        print(array_s[i][0])
        print(array_s[i][1])
        
main(array, n, m) 
'''




















