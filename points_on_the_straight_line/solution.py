from collections import Counter

# X and Y are list of integers
# A point is represented by (X[i], Y[i])
def max_points(X, Y):
    if len(X) < 2:
        return len(X)
        
    max_points = 0
    
    n = len(X)
    for i in range(n):
        x, y = X[i], Y[i]
        
        slope = []
        perp = 0
        same = 0
        for j in range(n):
            x1, y1 = X[j], Y[j]
            if x1 == x and y1 == y:
                same += 1
                continue
            if x1 == x:
                perp += 1
                continue
            slope.append(int((y1 - y) * 1000000000.0 / (x1 - x)))
        
        c = Counter(slope)
        for item in c:
            if c[item] + same > max_points:
                max_points = c[item] + same
        if perp + same > max_points:
            max_points = perp + same

    return max_points
        
        
    
    