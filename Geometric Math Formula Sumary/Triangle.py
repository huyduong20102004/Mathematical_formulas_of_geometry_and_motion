import math

# Hàm tính diện tích khi biết cạnh đáy và chiều cao
def dien_tich(a, h):
    return 0.5 * a * h

# Hàm tính chu vi khi biết ba cạnh
def chu_vi(a, b, c):
    return a + b + c

# Hàm tính chiều cao khi biết diện tích và cạnh đáy
def chieu_cao(S, a):
    return 2 * S / a

# Hàm tính cạnh đáy khi biết diện tích và chiều cao
def canh_day(S, h):
    return 2 * S / h

# Hàm tính diện tích bằng công thức Heron khi biết ba cạnh
def dien_tich_heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Ví dụ sử dụng các hàm
a = 5
b = 6
c = 7

S = dien_tich_heron(a, b, c)
P = chu_vi(a, b, c)
h = chieu_cao(S, a)
canh_day = canh_day(S, h)

print(f"Diện tích: {S}")
print(f"Chu vi: {P}")
print(f"Chiều cao: {h}")
print(f"Cạnh đáy: {canh_day}")
