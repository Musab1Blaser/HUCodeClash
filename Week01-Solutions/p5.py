for _ in range(int(input())):
    n = int(input())
    s = input()
    ctrs = [0,0,0,0] # A, B, C, D
    for guess in s:
        if guess != "?":
            ctrs[ord(guess) - ord('A')] += 1
    ans = min(ctrs[0], n) + min(ctrs[1], n) + min(ctrs[2], n) + min(ctrs[3], n)
    print(ans) 