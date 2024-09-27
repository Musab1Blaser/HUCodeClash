for _ in range(int(input())):
    s = input()
    counter = 0
    for letter in s:
        counter += int(letter)
    print(counter)