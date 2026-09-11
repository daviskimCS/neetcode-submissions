class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sContains = {}
        tContains = {}
        
        for sLetter in s:
            if sContains.get(sLetter) is not None:
                sContains.update({sLetter: sContains.get(sLetter) + 1})
            else:
                sContains.update({sLetter: 1})
        for tLetter in t:
            if tContains.get(tLetter) is not None:
                tContains.update({tLetter: tContains.get(tLetter) + 1})
            else:
                tContains.update({tLetter: 1})
            
        return sContains == tContains