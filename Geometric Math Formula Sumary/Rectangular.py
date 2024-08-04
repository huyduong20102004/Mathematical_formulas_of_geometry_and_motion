# Hàm tính diện tích xung quanh, diện tích toàn phần, diện tích quét vôi của hình hộp chữ nhật
def tinh_dien_tich(a, b, h):
    # Diện tích xung quanh (S_xq)
    S_xq = 2 * h * (a + b)
    
    # Diện tích toàn phần (S_tp)
    S_tp = 2 * (a * b + a * h + b * h)
    
    # Diện tích quét vôi (S_qv) - giả sử bao gồm toàn bộ các mặt
    S_qv = S_tp
    
    return S_xq, S_tp, S_qv

# Hàm tính thể tích và chiều cao mặt nước
def tinh_the_tich_va_chieu_cao(v, S_day):
    # Khối (thể tích)
    khoi = v / S_day
    
    # Chiều cao mặt nước đang có trong hồ
    chieu_cao = khoi
    
    return khoi, chieu_cao

# Hàm chính để nhập dữ liệu và tính diện tích
def main():
    # Nhập kích thước của hình hộp chữ nhật
    a = float(input("Nhập chiều dài (a): "))
    b = float(input("Nhập chiều rộng (b): "))
    h = float(input("Nhập chiều cao (h): "))
    
    # Tính diện tích
    S_xq, S_tp, S_qv = tinh_dien_tich(a, b, h)
    
    # In kết quả
    print(f"Diện tích xung quanh (S_xq): {S_xq}")
    print(f"Diện tích toàn phần (S_tp): {S_tp}")
    print(f"Diện tích quét vôi (S_qv): {S_qv}")
    
    # Nhập thêm dữ liệu để tính thể tích và chiều cao mặt nước
    v = float(input("Nhập thể tích nước đang có trong hồ (V): "))
    S_day = float(input("Nhập diện tích đáy hồ (S_đáy): "))
    
    # Tính thể tích và chiều cao mặt nước
    khoi, chieu_cao = tinh_the_tich_va_chieu_cao(v, S_day)
    
    # In kết quả
    print(f"Khối: {khoi}")
    print(f"Chiều cao mặt nước đang có trong hồ: {chieu_cao}")

if __name__ == "__main__":
    main()
