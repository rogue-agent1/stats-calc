#!/usr/bin/env python3
"""stats_calc - Statistical calculations: descriptive stats, distributions."""
import sys, math

def mean(data):
    return sum(data) / len(data)

def median(data):
    s = sorted(data)
    n = len(s)
    if n % 2: return s[n//2]
    return (s[n//2-1] + s[n//2]) / 2

def mode(data):
    from collections import Counter
    c = Counter(data)
    max_count = max(c.values())
    return [k for k, v in c.items() if v == max_count]

def variance(data, sample=True):
    m = mean(data)
    n = len(data)
    return sum((x - m)**2 for x in data) / (n - 1 if sample else n)

def stdev(data, sample=True):
    return math.sqrt(variance(data, sample))

def percentile(data, p):
    s = sorted(data)
    k = (len(s) - 1) * p / 100
    f = int(k)
    c = f + 1 if f + 1 < len(s) else f
    return s[f] + (k - f) * (s[c] - s[f])

def correlation(x, y):
    n = len(x)
    mx, my = mean(x), mean(y)
    num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    dx = math.sqrt(sum((xi-mx)**2 for xi in x))
    dy = math.sqrt(sum((yi-my)**2 for yi in y))
    return num / (dx * dy) if dx * dy > 0 else 0

def zscore(data):
    m, s = mean(data), stdev(data, sample=False)
    return [(x - m) / s if s > 0 else 0 for x in data]

def iqr(data):
    q1 = percentile(data, 25)
    q3 = percentile(data, 75)
    return q3 - q1

def test():
    d = [2, 4, 4, 4, 5, 5, 7, 9]
    assert abs(mean(d) - 5.0) < 0.01
    assert abs(median(d) - 4.5) < 0.01
    assert mode(d) == [4]
    assert abs(stdev(d) - 2.138) < 0.01
    assert abs(percentile(d, 50) - 4.5) < 0.01
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert abs(correlation(x, y) - 1.0) < 0.01
    z = zscore([10, 20, 30])
    assert abs(z[1]) < 0.01
    assert abs(iqr(d) - 1.5) < 0.5
    assert median([1]) == 1
    assert mean([5]) == 5
    print("All tests passed!")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("stats_calc: Statistics calculator. Use --test")
