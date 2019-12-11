def combinations(n, k):
    def recurse(i, li):
        if len(li) == k:
            result.append([x for x in li])
            return

        if i > n:
            return

        recurse(i+1, li+[i])
        recurse(i+1, li)

    result = []
    recurse(1, [])
    return result


if __name__ == "__main__":
    n, k = 4, 2
    print(combinations(n, k))
