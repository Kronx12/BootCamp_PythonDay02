import math


class TinyStatistician:
    def mean(x):
        if len(x) == 0:
            return None
        u = 0.0
        for xi in x:
            u += xi
        u /= len(x)
        return float(u)

    def median(x):
        if len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 != 0:
            return x[int(len(x) / 2)]
        else:
            return TinyStatistician.mean([x[int(len(x) / 2 - 1)],
                                          x[int(len(x) / 2)]])

    def quartiles(x, percentile):
        if len(x) == 0:
            return None
        x.sort()
        l1 = []
        l2 = []
        if len(x) % 2 != 0:
            l1 = x[:int(len(x) / 2)]
            l2 = x[int(len(x) / 2 + 1):]
        else:
            l1 = x[:int(len(x) / 2)]
            l2 = x[int(len(x) / 2):]
        if percentile == 25:
            return TinyStatistician.median(l1)
        elif percentile == 75:
            return TinyStatistician.median(l2)

    def var(x):
        if len(x) == 0:
            return None
        res = 0.0
        for i in x:
            res += (i - TinyStatistician.mean(x)) ** 2
        res /= len(x)
        return res

    def std(x):
        if len(x) == 0:
            return None
        return math.sqrt(TinyStatistician.var(x))


if __name__ == "__main__":
    print("Mean :")
    print(TinyStatistician.mean([1, 2, 3, 4, 5]))
    print(TinyStatistician.mean([]))
    print("\nMedian :")
    print(TinyStatistician.median([1, 4, 5, 2, 3]))
    print(TinyStatistician.median([1, 5, 3, 4, 2, 6]))
    print(TinyStatistician.median([]))
    print("\nQ1 :")
    print(TinyStatistician.quartiles([1, 4, 5, 2, 3], 25))
    print(TinyStatistician.quartiles([1, 5, 3, 4, 2, 6], 25))
    print(TinyStatistician.quartiles([], 25))
    print("\nQ3 :")
    print(TinyStatistician.quartiles([1, 4, 5, 2, 3], 75))
    print(TinyStatistician.quartiles([1, 5, 3, 4, 2, 6], 75))
    print(TinyStatistician.quartiles([], 75))
    print("\nVariance :")
    print(TinyStatistician.var([1, 4, 5, 2, 3]))
    print(TinyStatistician.var([1, 5, 3, 4, 2, 6]))
    print(TinyStatistician.var([]))
    print("\nStandard Deviation :")
    print(TinyStatistician.std([1, 4, 5, 2, 3]))
    print(TinyStatistician.std([1, 5, 3, 4, 2, 6]))
    print(TinyStatistician.std([]))
