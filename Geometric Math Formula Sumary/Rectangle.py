def tinh_chu_vi(dai, rong):
    return 2 * (dai + rong)

def tinh_dien_tich(dai, rong):
    return dai * rong

def tinh_chieu_dai_tu_chu_vi_va_rong(chu_vi, rong):
    return (chu_vi / 2) - rong

def tinh_chieu_rong_tu_chu_vi_va_dai(chu_vi, dai):
    return (chu_vi / 2) - dai

def tinh_chieu_dai_tu_dien_tich_va_rong(dien_tich, rong):
    return dien_tich / rong

def tinh_chieu_rong_tu_dien_tich_va_dai(dien_tich, dai):
    return dien_tich / dai

# Ví dụ sử dụng:
chieu_dai = 10
chieu_rong = 5
dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)

# Tính chu vi và diện tích
chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)

# Tính chiều dài từ chu vi và chiều rộng
chieu_dai_tu_chu_vi = tinh_chieu_dai_tu_chu_vi_va_rong(chu_vi, chieu_rong)

# Tính chiều rộng từ chu vi và chiều dài
chieu_rong_tu_chu_vi = tinh_chieu_rong_tu_chu_vi_va_dai(chu_vi, chieu_dai)

# Tính chiều dài từ diện tích và chiều rộng
chieu_dai_tu_dien_tich = tinh_chieu_dai_tu_dien_tich_va_rong(dien_tich, chieu_rong)

# Tính chiều rộng từ diện tích và chiều dài
chieu_rong_tu_dien_tich = tinh_chieu_rong_tu_dien_tich_va_dai(dien_tich, chieu_dai)

print(f"Chu vi: {chu_vi}")
print(f"Diện tích: {dien_tich}")
print(f"Chiều dài từ chu vi: {chieu_dai_tu_chu_vi}")
print(f"Chiều rộng từ chu vi: {chieu_rong_tu_chu_vi}")
print(f"Chiều dài từ diện tích: {chieu_dai_tu_dien_tich}")
print(f"Chiều rộng từ diện tích: {chieu_rong_tu_dien_tich}")

