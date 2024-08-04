def tinh_dien_tich_tam_giac_vuong(a, b):
    """
    Tính diện tích của tam giác vuông.

    Args:
    a (float): Độ dài của cạnh góc vuông thứ nhất.
    b (float): Độ dài của cạnh góc vuông thứ hai.

    Returns:
    float: Diện tích của tam giác vuông.
    """
    return 0.5 * a * b

# Ví dụ sử dụng
canh1 = 3.0
canh2 = 4.0
dien_tich = tinh_dien_tich_tam_giac_vuong(canh1, canh2)
print(f"Diện tích của tam giác vuông là: {dien_tich}")
