def check_sqrt(_min: int, _max: int, x: int):
    mid = int((_max + _min) / 2)
    if mid * mid > x:
        return check_sqrt(_min, mid, x)
    elif mid * mid == x:
        return mid
    else:
        if (mid+1) * (mid+1) > x:
            return mid
        if _max == 2:
            return check_sqrt(2, 2, x)
        return check_sqrt(mid, _max, x)


class SqrtX:
    @staticmethod
    def my_sqrt(x: int) -> int:
        if x == 1:
            return x
        _max = int(x / 2)
        _min = 1
        return check_sqrt(_min, _max, x)
