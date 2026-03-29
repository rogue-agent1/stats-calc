import sys, argparse, math

def mean(v): return sum(v)/len(v)
def median(v):
    s = sorted(v); n = len(s)
    return s[n//2] if n%2 else (s[n//2-1]+s[n//2])/2
def mode(v):
    from collections import Counter
    c = Counter(v)
    mx = max(c.values())
    return [k for k,v in c.items() if v == mx]
def stdev(v):
    m = mean(v)
    return math.sqrt(sum((x-m)**2 for x in v) / (len(v)-1))
def percentile(v, p):
    s = sorted(v)
    k = (len(s)-1) * p / 100
    f = int(k); c = f+1 if f+1 < len(s) else f
    return s[f] + (k-f) * (s[c]-s[f])

def main():
    p = argparse.ArgumentParser(description="Statistics calculator")
    p.add_argument("values", nargs="*", type=float)
    p.add_argument("-p", "--percentile", type=float)
    args = p.parse_args()
    vals = args.values or [float(x) for x in sys.stdin.read().split()]
    if not vals: print("No data"); return
    print(f"n:      {len(vals)}")
    print(f"sum:    {sum(vals):.4f}")
    print(f"mean:   {mean(vals):.4f}")
    print(f"median: {median(vals):.4f}")
    print(f"mode:   {mode(vals)}")
    print(f"min:    {min(vals):.4f}")
    print(f"max:    {max(vals):.4f}")
    print(f"range:  {max(vals)-min(vals):.4f}")
    if len(vals) > 1: print(f"stdev:  {stdev(vals):.4f}")
    print(f"p25:    {percentile(vals, 25):.4f}")
    print(f"p75:    {percentile(vals, 75):.4f}")
    print(f"p90:    {percentile(vals, 90):.4f}")

if __name__ == "__main__":
    main()
