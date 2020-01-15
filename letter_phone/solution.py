def letter_combinations(S):
    digit_map = {
        '0': ['0'],
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    N = len(S)
    result = []
    
    def recurse(i, li):
        if len(li) == N:
            result.append("".join([x for x in li]))
            return
        for ch in digit_map[S[i]]:
            li.append(ch)
            recurse(i+1, li)
            li.pop()
            
    recurse(0, [])
    
    return result
            
    
if __name__ == "__main__":
    S = "23"
    print(letter_combinations(S))
    
