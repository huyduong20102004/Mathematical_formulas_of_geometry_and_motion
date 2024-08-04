def tinh_van_toc(quang_duong, thoi_gian):
    """
    Tính vận tốc dựa vào quãng đường và thời gian.

    Tham số:
    quang_duong (float): Quãng đường đã đi (km).
    thoi_gian (float): Thời gian đã đi (giờ).

    Trả về:
    float: Vận tốc (km/h).
    """
    if thoi_gian == 0:
        return None  # Tránh chia cho 0
    return quang_duong / thoi_gian

def tinh_quang_duong(van_toc, thoi_gian):
    """
    Tính quãng đường dựa vào vận tốc và thời gian.

    Tham số:
    van_toc (float): Vận tốc (km/h).
    thoi_gian (float): Thời gian đã đi (giờ).

    Trả về:
    float: Quãng đường đã đi (km).
    """
    return van_toc * thoi_gian

def tinh_thoi_gian(quang_duong, van_toc):
    """
    Tính thời gian dựa vào quãng đường và vận tốc.

    Tham số:
    quang_duong (float): Quãng đường đã đi (km).
    van_toc (float): Vận tốc (km/h).

    Trả về:
    float: Thời gian đã đi (giờ).
    """
    if van_toc == 0:
        return None  # Tránh chia cho 0
    return quang_duong / van_toc

# Ví dụ sử dụng:
quang_duong = 100  # km
thoi_gian = 2  # giờ
van_toc = tinh_van_toc(quang_duong, thoi_gian)
print(f"Vận tốc: {van_toc} km/h")

van_toc = 50  # km/h
quang_duong = tinh_quang_duong(van_toc, thoi_gian)
print(f"Quãng đường: {quang_duong} km")

quang_duong = 100  # km
van_toc = 50  # km/h
thoi_gian = tinh_thoi_gian(quang_duong, van_toc)
print(f"Thời gian: {thoi_gian} giờ")
