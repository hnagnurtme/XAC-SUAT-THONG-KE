import matplotlib.pyplot as plt
import numpy as np
import math
import csv
data = []
with open('data3.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            try:
                data.append(float(row[0]))
            except ValueError:
                continue

def calculate_bin_edges(data):
    """
    Tính toán bin edges tự động cho histogram.
    
    :param data: Dữ liệu đầu vào.
    :return: List các bin edges.
    """
    num_bins = math.floor(math.sqrt(len(data)))  # Số lượng bins dựa trên số lượng dữ liệu
    print(f"Số lượng bins: {num_bins}")
    # Lấy giá trị nhỏ nhất và lớn nhất từ dữ liệu
    min_val = min(data)
    max_val = max(data)

    value = (max_val - min_val) / num_bins
    d = math.ceil(value * 100) / 100  # Làm tròn lên đến 2 chữ số thập phâ
    print(f"Khoảng cách giữa các bins: {d}")

    # Tạo bin edges từ desired_range_min đến desired_range_max
    bin_edges = [min_val + i * d for i in range(num_bins + 1)]

    # Làm tròn đến 2 chữ số thập phân
    bin_edges = [round(edge, 2) for edge in bin_edges]

    return bin_edges


bin_edges = calculate_bin_edges(data)

def plot_histogram(data, bin_edges):
    """
    Vẽ biểu đồ histogram với các đường dóng ngang qua mỗi cột.
    
    :param data: Dữ liệu đầu vào.
    :param bin_edges: Các khoảng bins cụ thể.
    """
    # Vẽ histogram với các cột có màu gradient
    n, bins, patches = plt.hist(data, bins=bin_edges, edgecolor='black', color='skyblue')

    # Thêm các đường dóng ngang qua các cột (ở mức tần số của các cột)
    for i in range(len(bins)-1):
        # Dựng một đường ngang tại tần số của cột với màu sắc đẹp
        plt.plot([bins[i], bins[i+1]], [n[i], n[i]], color='purple', linewidth=1.5, linestyle='--')

    # Thêm các nhãn vào cột và làm tròn đến 2 chữ số thập phân
    for i in range(len(patches)):
        height = patches[i].get_height()
        plt.annotate(f'{height:.2f}',
                     xy=(patches[i].get_x() + patches[i].get_width() / 2, height),
                     ha='center', va='bottom', fontsize=10, color='darkblue')

    # Thiết lập các mốc trên trục x và làm tròn các giá trị bin edges đến 2 chữ số thập phân
    plt.xticks(bin_edges, rotation=0)

    # Tăng cường hiệu ứng bóng cho các cột histogram
    for patch in patches:
        patch.set_alpha(0.7)  # Độ trong suốt của các cột
        patch.set_edgecolor('black')  # Đặt viền màu đen cho cột
        patch.set_linewidth(1.5)  # Đặt độ rộng viền

    # Thiết lập tiêu đề và nhãn với phông chữ lớn hơn
    plt.title('Biểu đồ tần số chiều dài bọ cánh cứng ', fontsize=14)
    plt.xlabel('Chiều dài (mm)', fontsize=12)
    plt.ylabel('Tần số', fontsize=12)

    # Hiển thị biểu đồ với layout chặt chẽ hơn
    plt.tight_layout()
    plt.show()


# Gọi hàm để vẽ histogram
plot_histogram(data, bin_edges)