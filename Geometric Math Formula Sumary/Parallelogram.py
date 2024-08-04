def hinh_binh_hanh(dai_day=None, chieu_cao=None, canh_ben=None, dien_tich=None):
    # Tính diện tích nếu có đáy và chiều cao
    if dien_tich is None and dai_day is not None and chieu_cao is not None:
        dien_tich = dai_day * chieu_cao
    
    # Tính chiều cao nếu có diện tích và đáy
    if chieu_cao is None and dien_tich is not None and dai_day is not None:
        chieu_cao = dien_tich / dai_day
    
    # Tính đáy nếu có diện tích và chiều cao
    if dai_day is None and dien_tich is not None and chieu_cao is not None:
        dai_day = dien_tich / chieu_cao
    
    # Tính chu vi nếu có đáy và cạnh bên
    if canh_ben is not None and dai_day is not None:
        chu_vi = 2 * (dai_day + canh_ben)
    else:
        chu_vi = None

    return {
        "Diện tích": dien_tich,
        "Chiều cao": chieu_cao,
        "Đáy": dai_day,
        "Chu vi": chu_vi,
    }

# Ví dụ sử dụng:
dai_day = 6
chieu_cao = 4
canh_ben = 5

ket_qua = hinh_binh_hanh(dai_day=dai_day, chieu_cao=chieu_cao, canh_ben=canh_ben)

print(f"Diện tích: {ket_qua['Diện tích']} cm²")
print(f"Chiều cao: {ket_qua['Chiều cao']} cm")
print(f"Đáy: {ket_qua['Đáy']} cm")
print(f"Chu vi: {ket_qua['Chu vi']} cm")
