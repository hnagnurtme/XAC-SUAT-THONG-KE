import matplotlib.pyplot as plt
import numpy as np
import math
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def calculate_bin_edges(data, num_bins=7):
    """
    Tính toán các bin_edges tự động từ dữ liệu, chia phạm vi thành số bin cụ thể.
    
    :param data: Dữ liệu đầu vào.
    :param num_bins: Số lượng bins (khoảng), mặc định là 7.
    :return: List các bin_edges.
    """
    min_val = min(data)
    max_val = max(data)
    
    # Sử dụng np.linspace để tạo ra num_bins khoảng đều nhau giữa min_val và max_val
    bin_edges = np.linspace(min_val, max_val, num_bins + 1)  # num_bins + 1 vì bao gồm cả điểm cuối

    # Làm tròn các bin_edges đến 2 chữ số thập phân
    bin_edges = np.round(bin_edges, 2)
    return bin_edges

def plot_histogram_with_horizontal_lines(data, bin_edges):
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
    plt.title('Biểu đồ tần số chiều dài bọ cánh cứng với các đường dóng ngang', fontsize=14)
    plt.xlabel('Chiều dài (mm)', fontsize=12)
    plt.ylabel('Tần số', fontsize=12)

    # Hiển thị biểu đồ với layout chặt chẽ hơn
    plt.tight_layout()
    plt.show()

# Dữ liệu chiều dài các con bọ cánh cứng lay tu data.csv
data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(float(row[0]))  # Chỉ lấy cột đầu tiên (chiều dài)



# Tính num_bins tự động từ dữ liệu
num_bins = math.ceil(math.sqrt(len(data)))  # Số lượng bins tự động theo quy tắc Sturges

# Tính toán các khoảng bin tự động từ dữ liệu
bin_edges = calculate_bin_edges(data, num_bins)

# Gọi hàm để vẽ histogram với các đường dóng ngang
plot_histogram_with_horizontal_lines(data, bin_edges)
