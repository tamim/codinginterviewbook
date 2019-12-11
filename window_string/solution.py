from collections import Counter, defaultdict

def minWindow1(S, T):
            
    def contains(s, t):
        for item in t:
            if s[item] < t[item]:
                return False
        return True
    
    t_counter = defaultdict(int)
    for c in T:
        t_counter[c] += 1
        
    left, right, len_s = 0, 0, len(S)
    min_left, min_right, min_len = -1, -1, len(S)+1
    
    s_counter = defaultdict(int)
    while right < len_s:
        while right < len_s:
            s_counter[S[right]] += 1
            if contains(s_counter, t_counter):
                break
            right += 1
            
        while left < right:
            s_counter[S[left]] -= 1
            if contains(s_counter, t_counter):
                left += 1
            else: # restore
                s_counter[S[left]] += 1
                break
            
        if contains(s_counter, t_counter) and (right - left < min_len):
            min_len = right - left
            min_left, min_right = left, right
            
        right += 1
        
    
    return S[min_left:min_right+1] if min_len < float('inf') else ""
                

def minWindow2(S, T):
    t_freq = Counter(T)
    different_chars = len(t_freq)

    s_freq = defaultdict(int)

    len_s = len(S)
    min_left, min_right, min_len = -1, -1, len_s+1

    matched = 0

    left = 0
    for right in range(len_s):
        ch_add = S[right]
        s_freq[ch_add] += 1
        if ch_add in t_freq and s_freq[ch_add] == t_freq[ch_add]:
            matched += 1
            
        while matched == different_chars and left <= right:
            ch_remove = S[left]
            
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left, min_right = left, right
                
            s_freq[ch_remove] -= 1
            if ch_remove in t_freq and s_freq[ch_remove] < t_freq[ch_remove]:
                matched -= 1
                
            left += 1

    if min_len == len_s+1:
        return ""

    return S[min_left:min_right+1]

if __name__ == "__main__":
    S, T = "ADOBECODEBANC", "ABC"
    print(minWindow1(S, T))
    print(minWindow2(S, T))