import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def read_data(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        data = list(map(float, line.strip().split()))
    return data

def draw_qq_plot(data):
    # Sắp xếp dữ liệu
    data_sorted = np.sort(data)
    n = len(data)

    # Tính quantile lý thuyết
    quantiles = (np.arange(1, n + 1) - 0.5) / n
    theoretical_quantiles = stats.norm.ppf(quantiles)  # z

    # Tính trung bình và độ lệch chuẩn mẫu
    mu = np.mean(data)
    sigma = np.std(data, ddof=1)  # dùng ddof=1 để tính theo mẫu

    # Tính đường chéo lý thuyết theo công thức giáo trình
    line = mu + sigma * theoretical_quantiles

    # Vẽ
    plt.figure(figsize=(8, 6))
    plt.plot(theoretical_quantiles, data_sorted, 'o', label='Dữ liệu thực tế')
    plt.plot(theoretical_quantiles, line, 'r--', label='Đường chéo lý thuyết: x = μz + σ')

    # Trang trí
    plt.xlabel('Quantile lý thuyết (z)')
    plt.ylabel('Giá trị thực tế (x)')
    plt.title('Q-Q Plot theo phân phối chuẩn N(μ, σ²)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Đọc dữ liệu và vẽ
filename = 'data.csv'
# filename = 'data-QQPlot2.csv'
# filename = 'data-QQPlot3.csv'
data = read_data(filename)
draw_qq_plot(data)