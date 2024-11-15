import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generar datos de ejemplo
data = [0.94, 6.02, 2.63, 1.83, 0.34, 0.34, 0.12, 4.02, 1.84, 2.46, 0.04, 7.01, 3.57, 0.48, 0.40, 0.41, 0.73, 1.49, 1.13, 0.69, 1.89, 0.30, 0.69, 0.91, 1.22, 3.08, 0.45, 1.44, 1.80, 0.10, 1.87, 0.37, 0.13, 5.95, 6.74, 3.30, 0.73, 0.21, 2.31, 1.16, 0.26, 1.37, 0.07, 4.80, 0.60, 2.17, 0.75, 1.47, 1.58, 0.41, 6.99, 2.98, 5.61, 4.50, 1.82, 5.10, 0.19, 0.44, 0.09, 0.79, 0.98, 0.63, 3.53, 0.88, 0.66, 1.56, 0.30, 3.24, 0.15, 8.67, 2.96, 0.44, 0.01, 3.38, 2.45, 2.61, 2.95, 0.15, 0.89, 0.25, 3.98, 1.95, 0.80, 0.13, 0.74, 0.79, 2.62, 2.03, 4.36, 1.28, 0.25, 2.50, 2.86, 1.65, 2.95, 1.36, 1.48, 1.12, 0.05, 0.23]
sum = 0
for i in data:
    sum+=i

# Histograma
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Histograma de Datos')
plt.show()

# Gráfico Q-Q
stats.probplot(data, dist="norm", plot=plt)
plt.title('Gráfico Q-Q')
plt.show()

# Prueba de Shapiro-Wilk
shapiro_test = stats.shapiro(data)
print(f"Shapiro-Wilk: Estadístico = {shapiro_test.statistic}, p-value = {shapiro_test.pvalue}")

shapiro_stat, shapiro_p =stats.shapiro(data)
print(f"Shapiro-Wilk p-valor: {shapiro_p}")

# Prueba de Anderson-Darling
anderson_result = stats.anderson(data, dist='norm')
print(f"Anderson-Darling estadístico: {anderson_result.statistic}, p-valores críticos: {anderson_result.critical_values}")

# Prueba de Kolmogorov-Smirnov
ks_stat, ks_p = stats.kstest(data, 'norm', args=(data.mean(), data.std()))
print(f"K-S p-valor: {ks_p}")