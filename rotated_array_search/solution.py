# https://www.interviewbit.com/problems/rotated-sorted-array-search/

def search(A, key):
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        if A[left] < A[mid] and key < A[mid] and key >= A[left]:
            right = mid - 1
        elif A[mid] < A[right] and key > A[mid] and key <= A[right]:
            left = mid + 1
        elif A[left] > A[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1