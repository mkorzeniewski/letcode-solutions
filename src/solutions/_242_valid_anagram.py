class ValidAnagram:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        s_dict, t_dict = dict(), dict()
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1

        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        return s_dict == t_dict
