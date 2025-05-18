def frequency(s):
    s = s.lower()
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d

def CheckAnagrams(s1, s2):
    d_s1 = frequency(s1)
    d_s2 = frequency(s2)
    if d_s1 == d_s2:
        return True
    else:   
        return False
    
inp1 = input("enter String 1:   ")
inp2 = input("Enter String 1:   ")
print(CheckAnagrams(inp1,inp2))
