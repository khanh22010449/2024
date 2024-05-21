n = int(input())
x = []
for _ in range(n):
    q, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    h = []
    for i in range(len(b)):
        if b[i] >= a[0]:
            s = a[0] - 1
            h.append(s)
        else:
            s = b[i]
            h.append(s)
    x.append(h)

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j] , end = " ")
    print()
