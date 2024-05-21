# Bài 34: Maximum distance 
# Cho mảng A[] gồm N phần tử và số nguyên dương K, nhiệm vụ của bạn là tìm khoảng cách lớn nhất giữa 2 chỉ số i,j  
# sao cho trị tuyệt đối của hiệu A[i] - A[j] bằng K
# Input Format:
# Dòng thứ nhất gồm N và K ; Dòng thứ 2 gồm các phần tử trong mảng A[]
# Constraints 
# 1 <= K <= N <= 10^6
# -10^6 <= A <= 10^6
# Output Format :
# In ra khoảng cách lớn nhất giữa i và j hoặc in ra -1 nếu không tồn tại cặp số như vậy 

# Sample Input 0
# 14 2 
# 0 1 3 0 4 0 0 3 3 -4 1 0 -4 3 
# Sample Output 0
# 12
from math import *
f = [0] * (10**6 + 1)

def init(a,n,k):
    for i in range(n):
        s = 0
        for j in range(n):
            if abs(a[j] - a[i]) == k:
                s = j - i 
        f[i] = s

def Binary_search(a,k):
    l = 0 
    r = len(a) - 1
    i = 1
    while(i):
        m = (l + r)//2
        if a[m] == k:
            i = 0
            return k
        elif a[m] > k:   # 0 1 2 3 4 5 6 7 8 9   k = 7 
            l = m + 1
        else:
            r = m - 1

        

if __name__ == '__main__':
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    init(a,n,k)
    if max(f) == 0:
        print("-1")
    else:
        print(max(f))

