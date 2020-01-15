"""
Accepted solution
"""
def hotel(arrive, depart, K):
    arrive.sort()
    depart.sort()
    
    count = 0
    n = len(arrive)
    
    i, j = 0, 0
    while i < n and j < n:
        if arrive[i] < depart[j]:
            count += 1
            if count > K:
                return False
            i += 1
        else:
            count -= 1
            j += 1

    return True


"""
Accepted and nicer looking solution (code)
"""
def hotel(arrive, depart, K):
    events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
    events.sort()

    count = 0

    for event in events:
        if event[1] == 1:
            count += 1
        else:
            count -= 1

        if count > K:
            return 0

    return 1


"""
Inefficent solution (why? ask yourself.)
"""
from collections import defaultdict

def hotel(arrive, depart, K):
    days = defaultdict(int)
    
    for start, end in zip(arrive, depart):
        for i in range(start, end):
            days[i] += 1
            if days[i] > K:
                return False

    return True
