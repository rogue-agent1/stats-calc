#!/usr/bin/env python3
"""Statistical calculator."""
import math

def mean(data):
    return sum(data) / len(data)

def median(data):
    s = sorted(data)
    n = len(s)
    if n % 2: return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2

def mode(data):
    counts = {}
    for x in data: counts[x] = counts.get(x, 0) + 1
    max_count = max(counts.values())
    return [k for k, v in sorted(counts.items()) if v == max_count]

def variance(data, sample=True):
    m = mean(data)
    ss = sum((x - m) ** 2 for x in data)
    return ss / (len(data) - 1) if sample else ss / len(data)

def stdev(data, sample=True):
    return math.sqrt(variance(data, sample))

def percentile(data, p):
    s = sorted(data)
    k = (len(s) - 1) * p / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c: return s[int(k)]
    return s[f] * (c - k) + s[c] * (k - f)

def correlation(x, y):
    n = len(x)
    mx, my = mean(x), mean(y)
    num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    dx = math.sqrt(sum((xi-mx)**2 for xi in x))
    dy = math.sqrt(sum((yi-my)**2 for yi in y))
    return num / (dx * dy) if dx * dy > 0 else 0

def describe(data):
    return {"count": len(data), "mean": mean(data), "median": median(data),
            "stdev": stdev(data), "min": min(data), "max": max(data),
            "q25": percentile(data, 25), "q75": percentile(data, 75)}

if __name__ == "__main__":
    import sys
    data = [float(x) for x in sys.argv[1:]] or [1,2,3,4,5,6,7,8,9,10]
    for k, v in describe(data).items():
        print(f"{k}: {v}")

def test():
    d = [1, 2, 3, 4, 5]
    assert mean(d) == 3.0
    assert median(d) == 3
    assert median([1,2,3,4]) == 2.5
    assert mode([1,1,2,3]) == [1]
    assert mode([1,1,2,2]) == [1, 2]
    assert abs(stdev(d) - 1.5811) < 0.001
    assert abs(variance(d) - 2.5) < 0.001
    assert percentile(d, 50) == 3
    assert abs(correlation([1,2,3], [1,2,3]) - 1.0) < 1e-10
    assert abs(correlation([1,2,3], [3,2,1]) - (-1.0)) < 1e-10
    desc = describe(d)
    assert desc["count"] == 5
    print("  stats_calc: ALL TESTS PASSED")
