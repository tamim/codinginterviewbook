def diff_possible1(A, k):
    n = len(A)
    i, j = 0, 1
    while i < n - 1:
        while j < n:
            if A[j] - A[i] == k:
                return True
            if A[j] - A[i] > k:
                break
            j += 1
        i += 1
        if i == j:
            j += 1
                   
    return False


def diff_possible2(A, k):
    n = len(A)
    i, j = 0, 1
    while i < n - 1 and j < n:
        if A[j] - A[i] == k and i != j:
            return True
        if A[j] - A[i] > k:
            i += 1
        else:
            j += 1
                
    return False
                
