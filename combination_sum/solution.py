# combination sum using duplicates
def combination_sum1(A, T):
    result = []

    A.sort()

    def recurse(i, li, S):
        if S == T:
            if li not in result:
                result.append([x for x in li])

        if S > T or i == len(A):
            return

        recurse(i, li+[A[i]], S+A[i])
        recurse(i+1, li, S)

    recurse(0, [], 0)

    return result


def combination_sum11(A, T):
    result = []

    A.sort()

    def recurse(i, li, S):
        if S == T:
            if li not in result:
                result.append([x for x in li])

        if S > T or i == n:
            return

        for j in range(i, n):
            recurse(j, li+[A[j]], S+A[j])

    n = len(A)
    recurse(0, [], 0)

    return result


# combination sum without using duplicates
def combination_sum2(A, T):
    result = []

    A.sort()

    def recurse(i, li, S):
        if S == T:
            if li not in result:
                result.append([x for x in li])

        if S > T or i == len(A):
            return

        recurse(i+1, li+[A[i]], S+A[i])
        recurse(i+1, li, S)

    recurse(0, [], 0)

    return result


if __name__ == "__main__":
    A, T = [2, 3, 6, 7], 7
    result = combination_sum11(A, T)
    print(result)
