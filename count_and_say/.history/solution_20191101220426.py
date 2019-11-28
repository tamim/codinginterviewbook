def countAndSay(N):
    # 1, 11, 21, 1211, 111222,
    
    s = "1"
    
    i = 1
    while i < N:
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
        
    return s

if __name__ == "__main__":
    result = dict()
    for i in range(1, 41):
        result[i] = countAndSay(i)

    #t = input()
    #t = int(t)
    t = 1

    for _ in range(t):
        #n = int(input())
        n = 20
        print(result[n])
