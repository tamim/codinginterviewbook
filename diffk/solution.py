# Brute force solution, A is sorted
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


# O(n) solution, A is sorted
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

# O(n) solution, A is not sorted, space complexity also O(n)
from collections import defaultdict

def diff_possible3(A, k):
    if k == 0:
        if len(A) < 2:
            return 0
        
    dd = defaultdict(int)
    
    for n in A:
        dd[n] += 1
        
    for n in A:
        dd[n] -= 1
        x = k + n
        if dd[x]:
            return 1
        dd[n] += 1
            
    return 0
            
