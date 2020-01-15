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

    def recurse(s, li):
        print(s, li)
        if s == "":
            result.append([x for x in li])

        n = len(s)
        for i in range(1, n+1):
            if is_palin(s[:i]):
                li.append(s[:i])
                recurse(s[i:], li)
                li.pop()

    result = []
    recurse(S, [])
    return result


if __name__ == "__main__":
    S = "aabcedde"
    print(partition(S))
