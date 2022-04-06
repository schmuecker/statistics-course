import math
import statistics

__author__ = "Tobias Schmücker"
__date__ = "04/2022"

data = [14, 24, 22, 19, 18, 36, 15, 29, 41, 17]

if __name__ == '__main__':
    # Sort data
    data_sorted = sorted(data)

    # Average
    average = sum(data) / len(data)

    # 0.25 Quartile
    index1 = math.ceil(len(data_sorted) * 0.25) - 1
    quartile1 = data_sorted[index1]

    # 0.5 Quantile (Median)
    index_median = int(len(data_sorted) * 0.5) - 1
    median = 1/2 * (data_sorted[index_median] + data_sorted[index_median + 1])

    # 0.75 Quartile
    index3 = math.ceil(len(data_sorted) * 0.75) - 1
    quartile3 = data_sorted[index3]

    # 0.9 Quantile
    index_4 = int(len(data_sorted) * 0.9) - 1
    quantile_4 = 1/2 * \
        (data_sorted[index_4] + data_sorted[index_4 + 1])

    print('Data:', data)
    print('Sorted data:', data_sorted)
    print('Average:', average)
    print('Index:', index1)
    print('0.25 Quartile:', quartile1)
    print('0.5 Quantile (Median):', median)
    print('0.75 Quartile:', quartile3)
    print('0.9 Quantile:', quantile_4)
