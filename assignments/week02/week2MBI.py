def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight(kg):"))
    height = float(input("Enter your height(m):"))

    bmi = weight/(height **2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
         category = "Overweight"
    else:
         category = "Obese"

    print(f"\nYour BMI is:{bmi:.1f}")
    print(f"Category:{category}")

main()