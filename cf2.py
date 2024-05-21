n = int(input())
a = []
for _ in range(n):
    b = list(map(int,input().split()))
    a.append(b)
x = []
for i in range (n):
    if a[i][1] * 2 < a[i][2] :
        print(f"{a[i][1] * a[i][0]}")
    elif a[i][0] % 2 == 1 and a[i][1] * 2 >= a[i][2]:
        print(f"{a[i][1] + a[i][2]*(a[i][0]//2)}")
    elif a[i][0] % 2 == 0 and a[i][1] * 2 >= a[i][2]:
        print(f"{a[i][2]*(a[i][0]//2)}")