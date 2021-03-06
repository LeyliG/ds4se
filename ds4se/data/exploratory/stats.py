# AUTOGENERATED! DO NOT EDIT! File to edit: dev/09_data.exploratory.stats.ipynb (unless otherwise specified).

__all__ = ['get_desc_stats', 'confidence_interval', 'report_stats']

# Cell
# Imports
from scipy.stats import sem, t, median_absolute_deviation as mad
from statistics import mean, median, stdev

# Cell
def get_desc_stats(l):
    return max(l), min(l), mean(l), median(l), stdev(l), mad(l)

# Cell
def confidence_interval(l, c = 0.95):
    n = len(l)
    m = mean(l)
    std_err = sem(l)
    h = std_err * t.ppf((1 + c) / 2, n - 1)

    start = m - h
    end = m + h

    return start, end

# Cell
def report_stats(l, c = 0.95):
    mini, maxi, μ, med, σ, med_σ = get_desc_stats(l)
    print("Max:", mini)
    print("Min:", maxi)
    print("Average:", μ)
    print("Median:", med)
    print("Standard Deviation:", σ)
    print("Median Absolute Deviation:", med_σ)

    start, end = confidence_interval(l, c = 0.95)
    print(f"{int(c * 100)}% of the data fall within {start} and {end}")