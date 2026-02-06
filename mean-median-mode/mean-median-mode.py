import numpy as np
from collections import Counter

def mean_median_mode(x):
    # Convert input to NumPy array
    x = np.array(x)
    
    # Mean and Median
    mean = float(np.mean(x))
    median = float(np.median(x))
    
    # Mode
    freq = Counter(x)
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    mode = float(min(modes))   # smallest mode if multiple
    
    return mean, median, mode
