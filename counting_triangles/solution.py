def count_triangles(A):
    if len(A) < 3:
        return 0
    
    A.sort()
    
    i, j, k, = 0, 1, 2
    count = 0
    
    n = len(A)
    while i < n - 2:
        j = i + 1
        k = i + 2
        while j < n - 1:
            two_sides = A[i] + A[j]
            while k < n:
                if two_sides <= A[k]:
                    break
                k += 1
            count += k - j - 1
        
            j += 1
        i += 1
                    
    return count
