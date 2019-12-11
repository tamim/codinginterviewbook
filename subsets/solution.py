"""
Generate all subsets of a set using recursion
"""
def subsets1(S):
    if S == []:
        return [[]]

    result = []

    def recurse(i, n, li):
        if i == n:
            result.append([x for x in li])
            return

        recurse(i+1, n, li+[S[i]])
        recurse(i+1, n, li)
                  
    recurse(0, len(S), [])
    return result


def subsets2(S):
    if S == []:
        return [[]]

    result = []

    def recurse(i, n, li):
        result.append([x for x in li])
        for j in range(i, n):
            li.append(S[j])
            recurse(j+1, n, li)
            li.pop()

    recurse(0, len(S), [])
    return result


"""
Generate all subsets of a set using a stack
"""
def subsets3(S):
    if S == []:
        return [[]]

    result = [[]]

    while len(S):
        temp_r = []
        x = S.pop()
        for r in result:
            temp_r.append(r + [])
            temp_r.append(r + [x])

        result = [item for item in temp_r]

    return result

"""
Generate all subset using loop and bit operation
"""
def subsets4(S):
    result = []

    subset_len = 2 ** len(S)

    for num in range(subset_len):
        li = []
        for i in range(len(S)):
            if num & (1 << i):
                li.append(S[i])
        result.append(li)

    return result


if __name__ == "__main__":
    print(subsets1([1, 2, 3]))
    print(subsets2([1, 2, 3]))
    print(subsets3([1, 2, 3]))
    print(subsets4([1, 2, 3]))
