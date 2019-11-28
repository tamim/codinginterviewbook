if __name__ == "__main__":
    result = dict()
    
    s = "1"
    i = 1
    result[i] = s

    while i < 41:
        t = ''
        
        lenS = len(s)
        j = 0
        while j < lenS:
            count = 1
            ch = s[j]
            while j < lenS - 1 and s[j] == s[j+1]:
                j += 1
                count += 1
            t += str(count) + ch
            j += 1
            
        s = t
        i += 1

        result[i] = s

    t = input()
    t = int(t)
    
    for _ in range(t):
        n = int(input())
        print(result[n])
