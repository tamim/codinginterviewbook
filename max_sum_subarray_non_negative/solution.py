# https://www.interviewbit.com/problems/max-non-negative-subarray/

def maxset(A):
    max_sum = -1
    start_indx, end_indx = -1, -1
    
    A.append(-1) # adding a negative number at the end
    
    i, n = 0, len(A)
    while i < n:
        while i < n and A[i] < 0:
            i += 1
        if i == n:
            break
        
        current_sum = 0
        count = 0
        while i < n and A[i] >= 0:
            current_sum += A[i]
            i += 1
            count += 1
        
        if current_sum > max_sum:
            max_sum = current_sum
            start_indx, end_indx = i - count, i - 1
        elif current_sum == max_sum and (end_indx - start_indx + 1 < count):
            start_indx, end_indx = i - count, i - 1
        
        
    if max_sum == -1:
        return []
            
    return A[start_indx:end_indx+1]
            