import matplotlib.pyplot as plt
from statistics import mean, multimode, median, quantiles, stdev, variance
from scipy.stats import iqr

# Klausur SS 2021
# Aufgabe 2.1
java = [25, 17, 25, 29, 20, 15, 11, 17, 16, 16]
ruby = [0, 4, 0, 0, 0, 2, 2, 1, 3, 0]
python = [11, 11, 13, 9, 10, 7, 3, 8, 9, 4]
print('data', java)
print('mode', multimode(java))
print('mean', mean(java))
print('median', median(java))
print('90% quantile', quantiles(java, n=10)[-1])
print('standard deviation', stdev(java))
print('interquartile range', iqr(java))
print('span range', max(java) - min(java))

# h) Schätzfunktion für Mittelwert
print('mean', mean(java))
# i) Schätzfunktion für Varianz
print('variance', variance(java))

# Aufgabe 2.2
# c)


plt.title('Java und Python')
plt.scatter(java, python, s=20, alpha=0.5)
plt.show()
plt.title('Java und Ruby')
plt.scatter(java, ruby, s=20, alpha=0.5)
plt.show()
plt.title('Python und Ruby')
plt.scatter(python, ruby, s=20, alpha=0.5)
plt.show()
