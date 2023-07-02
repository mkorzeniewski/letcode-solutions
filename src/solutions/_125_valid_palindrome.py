class ValidPalindrome:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c in "abcdefghijklmnoprstuyvwxzq0123456789")

        i = 0
        while i < len(s) / 2:
            if s[i] != s[len(s) - i - 1]:
                return False
            i = i + 1

        return True
