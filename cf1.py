t = int(input())
a = []
for _ in range(t):
    b = list(map(int,input().split()))
    a.append(b)
for i in range(t):
    if a[i][2] >= a[i][1] and a[i][1] >= 1 and a[i][0] >= a[i][2] and a[i][0] <= 50 and a[i][1] <= a[i][0]:
        print("NO")
    else:
        print("YES")