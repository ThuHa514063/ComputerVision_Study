# Computer Vision

## OpenCV

### Thư viện ```cv2```

**Cài đặt:** gõ lệnh để tải xuống thư viện cv2 trong terminal. Lệnh:
```
python -m pit install opencv-python
```

**Kiểm tra version:**
```
python -m pip show opencv-python
```

=> Kết quả:
```
Name: opencv-python
Version: 4.13.0.90
```

## XỬ LÝ ẢNH SỐ

### Giới thiệu 

#### Ảnh số là gì?

Một bức ảnh được định nghĩa là 1 hàm 2 chiều, f(x,y), trong đó x, y là tọa độ không gian (spatial coordinates). f dùng để định nghĩa cho **cường độ ánh sáng** hay ***mức xám*** (gray level) của ảnh tại tọa độ (x,y).

- Khi x, y và f là những giá trị ***hữu hạn*** và ***rời rạc*** thì bức ảnh đó được gọi là **ảnh số**.

- Trong đó tọa độ (x,y) gọi là ***phần tử ảnh*** hoặc gọi là **pixel**.

- Giá trị pixel thường hiển thị mức xám, màu sắc, độ cao,...

![alt text](image/pixel.jpg)

*Ví dụ về 1 pixel*

**Chú ý:** ***số hóa*** nhấn mạnh rằng ảnh số là *xấp xỉ* (gần giống) của ảnh thực.
