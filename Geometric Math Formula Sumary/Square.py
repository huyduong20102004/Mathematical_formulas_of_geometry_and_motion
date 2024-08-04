import math

# Hàm tính diện tích hình vuông
def tinh_dien_tich(a):
    return a ** 2

# Hàm tính chu vi hình vuông
def tinh_chu_vi(a):
    return 4 * a

# Hàm tính cạnh hình vuông từ diện tích
def tinh_canh_tu_dien_tich(S):
    return math.sqrt(S)

# Hàm tính cạnh hình vuông từ chu vi
def tinh_canh_tu_chu_vi(P):
    return P / 4

# Ví dụ sử dụng
canh = 5
dien_tich = tinh_dien_tich(canh)
chu_vi = tinh_chu_vi(canh)

print(f"Cạnh của hình vuông: {canh}")
print(f"Diện tích của hình vuông: {dien_tich}")
print(f"Chu vi của hình vuông: {chu_vi}")

# Tính cạnh từ diện tích hoặc chu vi
canh_tu_dien_tich = tinh_canh_tu_dien_tich(dien_tich)
canh_tu_chu_vi = tinh_canh_tu_chu_vi(chu_vi)

print(f"Cạnh tính từ diện tích: {canh_tu_dien_tich}")
print(f"Cạnh tính từ chu vi: {canh_tu_chu_vi}")

