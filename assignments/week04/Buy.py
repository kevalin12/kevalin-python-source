NUM_ITEMS=6

def main():
   prices = []

   
   print(f"Enter prices of {NUM_ITEMS} items:")
   for i in range(1, NUM_ITEMS + 1):
       price = float(input(f"Item {i}: "))
       prices.append(price)

   
   budget = float(input("\nEnter total budget: "))

   current_total = 0      
   bought_items = []      

   print()

   
   for i, price in enumerate(prices, start=1):
       
       if current_total + price <= budget:
           current_total += price
           bought_items.append(price)
           status = "buy"
       else:
           status = "cannot buy"
          

       price_display = int(price) if price.is_integer() else price
       print(f"Item {i} = {price_display} -> {status}")
       total_display = int(current_total) if float(current_total).is_integer() else current_total
       print(f"Current total = {total_display}\n")

   
   bought_display = [int(p) if p.is_integer() else p for p in bought_items]
   remaining = budget - current_total
   remaining_display = int(remaining) if float(remaining).is_integer() else remaining
   total_display = int(current_total) if float(current_total).is_integer() else current_total

   print(f"Bought items: {bought_display}")
   print(f"Total spent: {total_display}")
   print(f"Remaining budget: {remaining_display}")


if __name__ == "__main__":
    main()