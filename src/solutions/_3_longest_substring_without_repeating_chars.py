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
            longest = longest if i+1 - low_position < longest else i+1 - low_position

        return longest
