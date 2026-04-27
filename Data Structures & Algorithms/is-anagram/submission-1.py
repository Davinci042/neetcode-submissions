
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        S = {}
        T = {}
        
        if len(s) != len(t):
            return False
        i = 0
        while i < (len(alphabets)):
            s_count = 0
            t_count = 0

            for char in s:
                if alphabets[i] == char:
                    s_count += 1

            for char in t:
                if alphabets[i] == char:
                    t_count += 1

            if s_count > 0:
                S[alphabets[i]] = s_count

            if t_count > 0:
                T[alphabets[i]] = t_count

            i += 1
        
        return S == T



