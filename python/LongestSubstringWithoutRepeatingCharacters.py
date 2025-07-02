def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    l, r, max_length = 0, 0, 0
    while r < len(s):
        c = s[r]
        if c not in seen:
            seen.add(c)
            r += 1
        else:
            seen.remove(s[l])
            l += 1
        max_length = max(max_length, r - l)

    return max_length