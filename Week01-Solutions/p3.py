for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    tot = 0
    for i in range(n):
        if i%2 == 0:
            tot += a[i]
        else:
            tot -= a[i]
    print(tot)