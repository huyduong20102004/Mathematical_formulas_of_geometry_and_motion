def tinh_dien_tich_thanh_gieng(r, t):
    # Hằng số Pi
    pi = 3.14
    
    # Diện tích hình tròn nhỏ
    dien_tich_nho = r * r * pi
    
    # Bán kính của hình tròn lớn
    R = r + t
    
    # Diện tích hình tròn lớn
    dien_tich_lon = R * R * pi
    
    # Diện tích thành giếng
    dien_tich_thanh_gieng = dien_tich_lon - dien_tich_nho
    
    return dien_tich_thanh_gieng

# Giá trị cho trước
r = 5.0  # Bán kính của hình tròn nhỏ
t = 2.0  # Độ dày của thành giếng

dien_tich_thanh_gieng = tinh_dien_tich_thanh_gieng(r, t)
print(f"Diện tích thành giếng là: {dien_tich_thanh_gieng}")
