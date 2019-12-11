from collections import deque

def slidingMaximum(A, w):
    dq = deque()
    result = []
    
    if w >= len(A):
        result.append(max(A))
        return result
    
    for i in range(w):
        dq.append(A[i])
        
    max_n = max(dq)
    result.append(max_n)
    
    for i in range(w, len(A)):
        last_item = dq.popleft()
        dq.append(A[i])
        if A[i] >= max_n:
            max_n = A[i]
        elif last_item == max_n:
            max_n = max(dq)
        result.append(max_n)
        
    return result
            

if __name__ == "__main__":
    print(slidingMaximum([10, 9, 8, 7, 6, 5, 5, 5, 6, 7, 8, 9], 3))
    