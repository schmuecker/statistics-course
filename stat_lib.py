from statistics import mean, multimode, median, quantiles, stdev
from scipy.stats import iqr

java = [25, 17, 25, 29, 20, 15, 11, 17, 16, 16]
print('data', java)
print('mode', multimode(java))
print('mean', mean(java))
print('median', median(java))
print('90% quantile', quantiles(java, n=10)[-1])
print('standard deviation', stdev(java))
print('interquartile range', iqr(java))
print('span range', max(java) - min(java))