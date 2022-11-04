class RomanToInteger:

    @staticmethod
    def roman_to_int(s: str) -> int:
        result = 0
        size = len(s)
        for i in range(0, size):
            following = None if (i >= size - 1) else s[i + 1]
            match s[i]:
                case 'M':
                    result += 1000
                case 'D':
                    result += 500
                case 'C':
                    if following == 'D' or following == 'M':
                        result -= 100
                    else:
                        result += 100
                case 'L':
                    result += 50
                case 'X':
                    if following == 'L' or following == 'C':
                        result -= 10
                    else:
                        result += 10
                case 'V':
                    result += 5
                case 'I':
                    if following == 'V' or following == 'X':
                        result -= 1
                    else:
                        result += 1
        return result
