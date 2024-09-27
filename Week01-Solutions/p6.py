for _ in range(int(input())):
    x,y,k = map(int, input().split())
    if k%2:
        print(x, y)
    for i in range(k//2):
        print(x - (i + 1), y)
        print(x + (i + 1), y)
