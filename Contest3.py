def chk(edges, a, b):
    return (a, b) in edges or (b, a) in edges


n, m = map(int, input().split())
a = []

for i in range(m):
    a.append(tuple(map(int, input().split())))

vert = []
color = [0] * n
ks = 0
nc = 1

while 0 in color:
    i = 0
    while i < n and color[i] != 0:
        i += 1
    if i >= n:
        break
    else:
        vert.append(i)
        color[i] = nc
        while len(vert) != 0:
            f = 0
            for i in range(n):

                if chk(a, i + 1, vert[-1] + 1) and color[i] == 0:
                    vert.append(i)
                    color[i] = nc
                    f = 1
                    break
            if f == 0:
                vert.pop()
        ks += 1
        nc += 1
i = 1
while i in color:
    print(color.count(i))
    for j in range(n):
        if color[j] == i:
            print(j + 1, end=' ')
    print()
    i += 1