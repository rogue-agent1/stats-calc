#!/usr/bin/env python3
"""stats_calc: Statistical calculations (mean, median, stdev, percentile, correlation)."""
import math, sys

def mean(data): return sum(data) / len(data)

def median(data):
    s = sorted(data); n = len(s)
    if n % 2 == 1: return s[n//2]
    return (s[n//2-1] + s[n//2]) / 2

def variance(data, ddof=1):
    m = mean(data)
    return sum((x - m)**2 for x in data) / (len(data) - ddof)

def stdev(data, ddof=1): return math.sqrt(variance(data, ddof))

def percentile(data, p):
    s = sorted(data); n = len(s)
    k = (p / 100) * (n - 1)
    f = int(k); c = min(f + 1, n - 1)
    return s[f] + (k - f) * (s[c] - s[f])

def correlation(x, y):
    n = len(x); mx, my = mean(x), mean(y)
    cov = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    sx = math.sqrt(sum((xi-mx)**2 for xi in x))
    sy = math.sqrt(sum((yi-my)**2 for yi in y))
    if sx == 0 or sy == 0: return 0
    return cov / (sx * sy)

def linear_regression(x, y):
    n = len(x); mx, my = mean(x), mean(y)
    ss_xy = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    ss_xx = sum((xi-mx)**2 for xi in x)
    if ss_xx == 0: return (my, 0)
    slope = ss_xy / ss_xx
    intercept = my - slope * mx
    return (intercept, slope)

def test():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert mean(data) == 5.0
    assert median(data) == 4.5
    assert abs(stdev(data) - 2.138) < 0.001
    assert percentile(data, 50) == 4.5
    assert percentile(data, 0) == 2
    assert percentile(data, 100) == 9
    # Correlation
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert abs(correlation(x, y) - 1.0) < 1e-9
    # Regression
    intercept, slope = linear_regression(x, y)
    assert abs(slope - 2.0) < 1e-9
    assert abs(intercept - 0.0) < 1e-9
    # Anti-correlation
    y2 = [10, 8, 6, 4, 2]
    assert abs(correlation(x, y2) - (-1.0)) < 1e-9
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Usage: stats_calc.py test")
