from collections import deque


class LongestSubstring:
    @staticmethod
    def longest_substring(s: str) -> int:
        longest = 0
        control_map = {}
        low_position = 0
        for i in range(0, len(s)):
            if s[i] in control_map and control_map[s[i]] >= low_position:
                low_position = control_map[s[i]] + 1
            control_map[s[i]] = i
            longest = longest if i + 1 - low_position < longest else i + 1 - low_position

        return longest


    @staticmethod
    def longest_substring_set(s) -> int:
        i, j, _max = 0, 0, 0
        substr = set()

        while j < len(s):
            if s[j] not in substr:
                substr.add(s[j])
                j = j+1
                _max = max(_max, len(substr))
            else:
                substr.remove(s[i])
                i = i+1

        return _max
