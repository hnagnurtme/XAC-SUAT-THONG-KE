import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu ngẫu nhiên cho 27 màn
players_passed =[200, 300, 450, 600, 800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800,
                  1700, 1600, 1500, 1400, 1300, 1200, 1000, 800, 600, 450, 300, 200, 100, 50]
screen_numbers = np.arange(1, 28)

# Vẽ histogram với các cột kề sát nhau
plt.figure(figsize=(10, 6))
plt.bar(screen_numbers, players_passed, width=0.98, color='lightgreen', edgecolor='black')
plt.title('Số lượng người vượt qua mỗi màn game (Histogram)')
plt.xlabel('Màn game')
plt.ylabel('Số người vượt qua')
plt.xticks(screen_numbers)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

# In dữ liệu để kiểm tra
print("Số người vượt qua mỗi màn:", players_passed)
print("Tổng số người:", sum(players_passed))