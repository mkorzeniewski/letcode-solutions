from typing import List


class LongestCommonPrefix:
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        min_size = min([len(s) for s in strs])
        prefix = strs[0][:min_size]
        for s in strs:
            for i in reversed(range(len(prefix))):
                if s[i] != prefix[i]:
                    prefix = prefix[:i]

        return prefix
