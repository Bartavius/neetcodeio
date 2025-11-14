from typing import List


class Solution:

    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}{self.delimiter}{word}"
        print('encoded:', res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c != self.delimiter:
                n += c
            else:
                end = i + int(n)
                n = ""
                res.append(s[i+1:end+1])
                i = end
            i += 1
        print('decoded:', res)
        return res
        
