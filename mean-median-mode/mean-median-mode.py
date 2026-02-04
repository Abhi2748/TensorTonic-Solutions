import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    arr = np.asarray(x, dtype=float)
    mean = np.mean(arr)
    # print("mean=", mean)
    median = np.median(arr)
    # print("median=", median)

    counts = Counter(arr)
    max_freq = max(counts.values())
    mode = min(val for val, freq in counts.items() if freq == max_freq)
    # print("mode=",mode)
    return mean, median, mode      

    