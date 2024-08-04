def tinh_dien_tich(d1, d2):
    """
    Tính diện tích hình thoi từ hai đường chéo.
    
    :param d1: Độ dài của đường chéo thứ nhất
    :param d2: Độ dài của đường chéo thứ hai
    :return: Diện tích của hình thoi
    """
    return (d1 * d2) / 2

def tinh_tich_duong_cheo(d1, d2):
    """
    Tính tích của hai đường chéo.
    
    :param d1: Độ dài của đường chéo thứ nhất
    :param d2: Độ dài của đường chéo thứ hai
    :return: Tích của hai đường chéo
    """
    return d1 * d2

# Ví dụ sử dụng
d1 = 10  # Đường chéo thứ nhất
d2 = 8   # Đường chéo thứ hai

dien_tich = tinh_dien_tich(d1, d2)
tich_duong_cheo = tinh_tich_duong_cheo(d1, d2)

print(f"Diện tích hình thoi: {dien_tich}")
print(f"Tích của hai đường chéo: {tich_duong_cheo}")
