from collections import defaultdict 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def is_anagram(dt1, dt_target):
            for key in dt_target:
                if dt1[key] != dt_target[key]:
                    return False
            return True   
        
        n = len(s)
        m = len(p)
        if n < m:
            return []
        
        dt_p = defaultdict(int)
        for c in p:
            dt_p[c] += 1
            
        dt_s = defaultdict(int)
        for c in s[:m]:
            dt_s[c] += 1
                
        result = []
        prev = ""
        if is_anagram(dt_s, dt_p):
            result.append(0)
            prev = s[0]
        
        dt_s[s[0]] -= 1
        
        for i in range(1, n-m+1):
            last_indx = i+m-1
            last = s[last_indx]
            
            if last == prev:
                result.append(i)
                prev = s[i]
                dt_s[last] += 1
                dt_s[prev] -= 1
                continue
            
            dt_s[last] += 1
            
            if prev == "" and is_anagram(dt_s, dt_p):
                result.append(i)
                prev = s[i]
            else:
                prev = ""
                
            dt_s[s[i]] -= 1
            
                
        return result
        