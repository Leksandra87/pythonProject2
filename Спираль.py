n = int(input())
a = [i for i in range(1, n ** 2 + 1)]
b = [[0 for j in range(n)] for i in range(n)]
x = 0
k = n
s = n ** 2
while s > 0:
    for j in range(n):
        b[len(b) - k][j + (len(b) - k)] = a[x]
        x += 1
        s -= 1
    n -= 1
    k -= 1
    for i in range(n):
        b[i + (len(b) - k)][k - len(b)] = a[x]
        x += 1
        s -= 1
    for j in range(n):
        b[k - len(b)][k - 1 - j] = a[x]
        x += 1
        s -= 1
    n -= 1
    for i in range(n):
        b[(k - 1 - len(b)) - i][len(b) - (k + 1)] = a[x]
        x += 1
        s -= 1
for i in range(len(b)):
    for j in range(len(b)):
        print(b[i][j], end=' ')
    print()
