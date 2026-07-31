 
def calculate_tax(income):
    brackets = [
        (150000, 0.00),
        (300000, 0.05),
        (500000, 0.10),
        (750000, 0.15),
        (1000000, 0.20),
        (2000000, 0.25),
        (5000000, 0.30),
        (float('inf'), 0.35),
    ]

    total_tax = 0
    lower = 0
    details = []  # store tax details per bracket

    for upper, rate in brackets:
        if income > lower:
            taxable = min(income, upper) - lower
            tax = taxable * rate
            total_tax += tax
            if taxable > 0:
                details.append((lower, min(income, upper), rate, tax))
            lower = upper
        else:
            break

    return total_tax, details


def show_result(name, income):
    total_tax, details = calculate_tax(income)
    after_tax = income - total_tax
    effective_rate = (total_tax / income * 100) if income > 0 else 0

    print(f"\n=== Tax Calculation Result{name} ===")
    print("\nTax Breakdown")
    print()
    for lower, upper, rate, tax in details:
        print(f"{lower:,.0f} - {upper:,.0f}\t\t{tax:,.0f} Baht")

    print(f"\nTotal Tax\t\t{total_tax:,.0f} Baht")
    print(f"Net Income After Tax\t{after_tax:,.0f} Baht")
    print(f"Effective Tax Rate = {effective_rate:.2f}%")

    return total_tax, after_tax, effective_rate


def calculate_single():
    income = float(input("Enter net income : "))
    show_result("", income)


def calculate_multiple():
    n = int(input("Enter number of people : "))
    summary = []

    for i in range(1, n + 1):
        name = input(f"Enter name for person {i} : ").strip()
        if not name:
            name = f"Person {i}"
        income = float(input(f"Enter net income for {name} : "))
        total_tax, after_tax, effective_rate = show_result(f" ({name})", income)
        summary.append((name, income, total_tax, after_tax, effective_rate))

    # Summary for all people
    print("\n=== Summary for All ===")
    print(f"{'Name':<15}{'Net Income':>15}{'Total Tax':>15}{'After Tax Income':>20}{'Effective Rate':>18}")
    for name, income, total_tax, after_tax, effective_rate in summary:
        print(f"{name:<15}{income:>15,.0f}{total_tax:>15,.0f}{after_tax:>20,.0f}{effective_rate:>17.2f}%")


def main():
    print("=== Personal Income Tax Calculator ===")
    print("1. Calculate tax for one person")
    print("2. Calculate tax for multiple people")
    choice = input("Select menu (1/2) : ").strip()

    if choice == "1":
        calculate_single()
    elif choice == "2":
        calculate_multiple()
    else:
        print("Please select only 1 or 2")


if __name__ == "__main__":
    main()