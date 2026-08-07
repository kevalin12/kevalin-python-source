def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 8.5* height * base
    print(f"triangle with height {height} and base {base}")
    print(f"Area = {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

#จากตัวอย่างให้สร้าง function สำหรับพื้นที่วงกลม
def calculate_circle_radiu(Radius, Area):
    """Calculates and displays circle  radius"""
    area = 8.5* height * base
    print(f"circle  with height {height} and base {base}")
    print(f"Radiu = {height} × {base} = {radiu}")
    print()

print("Calculating circle  radius:")
calculate_circle_radiu(5, 3)
calculate_circle_radiu(10, 7)

def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()