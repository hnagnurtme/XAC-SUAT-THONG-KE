# Biểu đồ Histogram với Đường Dóng Ngang từ Dữ Liệu CSV

Đoạn mã Python này đọc dữ liệu số (ví dụ: chiều dài cơ thể bọ cánh cứng) từ tệp `data.csv`, tự động tính toán các khoảng bin của biểu đồ histogram, và vẽ biểu đồ với các đường dóng ngang qua từng cột. Biểu đồ được thiết kế để vừa dễ hiểu vừa rõ ràng, giúp người dùng phân tích dữ liệu dễ dàng hơn.

## 🔍 Tính Năng

- **Tính toán bin tự động** sử dụng phương pháp quy tắc căn bậc hai (quy tắc Sturges).
- **Vẽ biểu đồ histogram** với các khoảng bin được tính toán.
- **Đường dóng ngang** giúp dễ dàng so sánh giữa các cột.
- **Ghi chú giá trị tần số** làm tròn đến 2 chữ số thập phân.
- **Tăng cường hình ảnh**: cột histogram có màu gradient, viền đậm, hiệu ứng bóng.

## 📊 Ứng Dụng

Đoạn mã này đặc biệt hữu ích để phân tích các phép đo sinh học hoặc bất kỳ dữ liệu số liên tục nào được lưu trữ trong tệp `.csv` — ví dụ, chiều dài cơ thể của bọ cánh cứng, chiều cao cây, hoặc các phép đo trong nghiên cứu khoa học.

## 📋 Cách Sử Dụng

1. **Chuẩn bị dữ liệu**: Tạo một tệp `data.csv` chứa dữ liệu chiều dài (hoặc bất kỳ số liệu nào bạn muốn phân tích). Mỗi giá trị cần được ghi trên một dòng riêng biệt trong tệp.

2. **Cài đặt thư viện**: Đảm bảo rằng bạn đã cài đặt các thư viện cần thiết:
    ```bash
    pip install matplotlib numpy watchdog
    ```

3. **Chạy mã**:
    Sau khi chuẩn bị tệp dữ liệu, bạn chỉ cần chạy đoạn mã Python:
    ```bash
    python your_script.py
    ```
    Mã sẽ đọc dữ liệu từ `data.csv`, tính toán các khoảng bin, và vẽ biểu đồ histogram với các đường dóng ngang.

## 🛠️ Cấu Trúc Mã

- `calculate_bin_edges(data, num_bins=7)`: Hàm tính toán các khoảng bin tự động từ dữ liệu đầu vào.
- `plot_histogram_with_horizontal_lines(data, bin_edges)`: Hàm vẽ biểu đồ histogram với các đường dóng ngang tại tần số của các cột.

## 📄 Lưu Ý

- Đảm bảo rằng tệp `data.csv` nằm trong cùng thư mục với đoạn mã.
- Tệp dữ liệu cần có một cột chứa giá trị số, và mỗi giá trị cần được ghi trên một dòng riêng biệt.

---