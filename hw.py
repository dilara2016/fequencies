def frequency(s):
    s = s.lower()
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d

def removeNonRepeated(s):
    s = s.strip().lower()
    freq = frequency(s)
    result = ""
    for i in range(len(s)):
        if freq[s[i]] > 1:
            result += s[i]
    return result

inp = input("Enter a word: ")
print("output: ", removeNonRepeated(inp))
