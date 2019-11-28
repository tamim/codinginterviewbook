def sqrt(n):
    left = 1
    right = n
    
    rt = 0
    while left <= right:
        mid = (left + right) // 2
        sqr = mid * mid
        if sqr == A:
            return mid
        elif sqr < A:
            nextsqr = (mid+1) * (mid+1)
            if nextsqr > A:
                return mid
            
        if sqr < A:
            rt = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return rt