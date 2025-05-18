def cw(s):
    c = 0
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            c += 1

    return c + 1

inp = input("Enter String:  ")
print("Number of words: ", cw(inp))
