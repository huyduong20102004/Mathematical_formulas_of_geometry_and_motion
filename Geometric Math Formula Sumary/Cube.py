# Hàm tính diện tích xung quanh, diện tích toàn phần, thể tích của hình lập phương
def tinh_dien_tich_va_the_tich(a):
    # Diện tích xung quanh (S_xq)
    S_xq = (a * a) * 4
    
    # Diện tích toàn phần (S_tp)
    S_tp = (a * a) * 6
    
    # Thể tích (V)
    V = a * a * a
    
    return S_xq, S_tp, V

# Hàm tính cạnh từ diện tích xung quanh và diện tích toàn phần
def tinh_canh_tu_dien_tich(S_xq, S_tp):
    # Tính cạnh từ diện tích xung quanh
    a_tu_xq = (S_xq / 4) ** 0.5
    
    # Tính cạnh từ diện tích toàn phần
    a_tu_tp = (S_tp / 6) ** 0.5
    
    return a_tu_xq, a_tu_tp

# Hàm chính để nhập dữ liệu và tính toán
def main():
    # Nhập cạnh của hình lập phương
    a = float(input("Nhập cạnh của hình lập phương (a): "))
    
    # Tính diện tích và thể tích
    S_xq, S_tp, V = tinh_dien_tich_va_the_tich(a)
    
    # In kết quả
    print(f"Diện tích xung quanh (S_xq): {S_xq}")
    print(f"Diện tích toàn phần (S_tp): {S_tp}")
    print(f"Thể tích (V): {V}")
    
    # Nhập diện tích xung quanh và diện tích toàn phần để tính cạnh
    S_xq_nhap = float(input("Nhập diện tích xung quanh (S_xq): "))
    S_tp_nhap = float(input("Nhập diện tích toàn phần (S_tp): "))
    
    # Tính cạnh từ diện tích xung quanh và diện tích toàn phần
    a_tu_xq, a_tu_tp = tinh_canh_tu_dien_tich(S_xq_nhap, S_tp_nhap)
    
    # In kết quả
    print(f"Cạnh tính từ diện tích xung quanh: {a_tu_xq}")
    print(f"Cạnh tính từ diện tích toàn phần: {a_tu_tp}")

if __name__ == "__main__":
    main()
