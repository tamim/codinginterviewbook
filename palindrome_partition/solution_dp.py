from collections import defaultdict

def partition(S):  
    def is_palin(s):
        if len(s) <= 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1

        return 1

    def recurse(s, start, end):
        if start > end:
            return []
        if table[start, end] != []:
            return table[start, end]

        result = []
        for i in range(start+1, end):
            part2 = recurse(s, i, end)
            if is_palin(s[start:i]):
                for item in part2:
                    result.append([s[start:i]]+item)

        if is_palin(s[start:end]):
            result.append([s[start:end]])
        
        table[start, end] = result
        return result
    
    n = len(S)
    table = defaultdict(list)
    result = recurse(S, 0, n)
    for item in table.keys():
        print(item, table[item])
    return result

def palindrome_partition(S):
    def is_palindrome(s):
        return s == s[::-1]

    n = len(S)

    table = defaultdict(list)
    
    table[n-1, n].append([S[n-1]])
    
    for i in range(n-2, -1, -1):
        for j in range(i, n):
            if is_palindrome(S[i:j+1]):
                if j + 1 == n:
                    table[i, n].append([S[i:j+1]])
                for li in table[j+1, n]:
                    table[i, n].append([S[i:j+1]]+li)
    for k in table:
        print(k, table[k])


if __name__ == "__main__":
    S = "aabcedde"
    #print(partition(S))
    palindrome_partition(S)
