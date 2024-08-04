def tinh_dien_tich_hinh_thang_vuong(day_lon, day_nho, chieu_cao):
    dien_tich = 0.5 * (day_lon + day_nho) * chieu_cao
    return dien_tich

# Ví dụ sử dụng
day_lon = 8  # Chiều dài của đáy lớn
day_nho = 5   # Chiều dài của đáy nhỏ
chieu_cao = 4 # Chiều cao

dien_tich = tinh_dien_tich_hinh_thang_vuong(day_lon, day_nho, chieu_cao)
print(f"Diện tích của hình thang vuông là: {dien_tich} cm²")
