# Hàm tính diện tích của hình thang
def tinh_dien_tich_hinh_thang(a, b, h):
    return 0.5 * (a + b) * h

# Hàm tính chiều cao của hình thang từ diện tích
def tinh_chieu_cao_hinh_thang(dien_tich, a, b):
    return (2 * dien_tich) / (a + b)

# Ví dụ sử dụng
a = 5  # Độ dài cạnh đáy lớn
b = 3  # Độ dài cạnh đáy nhỏ
h = 4  # Chiều cao

# Tính diện tích
dien_tich = tinh_dien_tich_hinh_thang(a, b, h)
print(f"Diện tích của hình thang là: {dien_tich}")

# Tính chiều cao từ diện tích
chiều_cao = tinh_chieu_cao_hinh_thang(dien_tich, a, b)
print(f"Chiều cao của hình thang là: {chiều_cao}")
