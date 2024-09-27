for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    twos = 0 # number of twos in my list
    for num in a:
        if num == 2:
            twos += 1

    if twos%2:
        print(-1)
    else:
        target = twos//2
        lh2 = 0
        for idx in range(n):
            if a[idx] == 2:
                lh2 += 1
            if lh2 == target:
                print(idx+1)
                break

