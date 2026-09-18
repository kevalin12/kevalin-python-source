def calculate_electricity_cost(units):

   cost = 0

   if units <= 50:
       cost = units * 2.50

   elif units <= 100:
       cost = (50 * 2.50) + ((units - 50) * 3.00)

   elif units <= 200:
       cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50)

   else:
       cost = (50 * 2.50) + (50 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00)

   service_charge = 25
   total = cost + service_charge

   return cost, service_charge, total


while True:

   print("\n===== โปรแกรมคำนวณค่าไฟฟ้า =====")
   print("1. คำนวณค่าไฟ")
   print("2. ออกจากโปรแกรม")

   choice = input("เลือกเมนู: ")

   if choice == "1":

       units = float(input("กรอกจำนวนหน่วยไฟฟ้า: "))

       if units < 0:
           print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
           continue

       cost, service, total = calculate_electricity_cost(units)

       print("\nรายละเอียดค่าไฟ:")
       print(f"ค่าไฟฟ้า: {cost:.2f} บาท")
       print(f"ค่าบริการ: {service:.2f} บาท")
       print(f"รวมค่าไฟทั้งสิ้น: {total:.2f} บาท")

   elif choice == "2":

       print("ออกจากโปรแกรม")
       break

   else:
       print("กรุณาเลือกเมนู 1 หรือ 2")