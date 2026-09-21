#mycode
try:
    num1 = float(input("ตัวเลขที่ 1 : "))
    num2 = float(input("ตัวเลขที่ 2 : "))
    operator = input("เครื่องหมาย (+ , - , * , /) : ")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น ( + - * / ) เท่านั้น")
    print(f"{num1} {operator} {num2} = {result}")
except ValueError as e:
    print(f"เกิดข้อผิดพลาด: {e}")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")