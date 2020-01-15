from heapq import heapify, heappop, heappush

def max_chololates(N, K, A):
    h = []
    for item in A:
        heappush(h, item * -1)

    max_choc = 0

    for _ in range(K):
        current_choc = heappop(h)
        current_choc *= -1
        max_choc += current_choc
        current_choc = current_choc // 2
        heappush(h, current_choc * -1)

    return max_choc
    
if __name__ == "__main__":
    print(max_chololates(2, 3, [6, 5]))