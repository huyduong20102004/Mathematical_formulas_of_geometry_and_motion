import math

def calculate_circle_properties(radius):
    # Tính diện tích
    area = math.pi * (radius ** 2)
    
    # Tính chu vi
    circumference = 2 * math.pi * radius
    
    # Tính đường kính
    diameter = 2 * radius
    
    return area, circumference, diameter

def radius_from_area(area):
    return math.sqrt(area / math.pi)

def radius_from_circumference(circumference):
    return circumference / (2 * math.pi)

# Ví dụ sử dụng hàm với bán kính là 5
radius = 5
area, circumference, diameter = calculate_circle_properties(radius)

print(f"Diện tích: {area:.2f}")
print(f"Chu vi: {circumference:.2f}")
print(f"Đường kính: {diameter:.2f}")
print(f"Bán kính: {radius:.2f}")

# Ví dụ tính bán kính từ diện tích và chu vi
area_example = 78.54
circumference_example = 31.42

radius_from_area_example = radius_from_area(area_example)
radius_from_circumference_example = radius_from_circumference(circumference_example)

print(f"Bán kính từ diện tích (area = {area_example}): {radius_from_area_example:.2f}")
print(f"Bán kính từ chu vi (circumference = {circumference_example}): {radius_from_circumference_example:.2f}")

