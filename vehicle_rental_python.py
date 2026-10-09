print("=== VEHICLE RENTAL SYSTEM ===")

customer_name = input("Enter customer name: ")
vehicle_type = input("Enter vehicle type: ")
rental_days = int(input("Enter number of days: "))
daily_rate = float(input("Enter daily rental rate: "))

total_cost = rental_days * daily_rate

print("\n=== RENTAL SUMMARY ===")
print("Customer:", customer_name)
print("Vehicle:", vehicle_type)
print("Rental Days:", rental_days)
print("Daily Rate: ₱{:.2f}".format(daily_rate))
print("Total Cost: ₱{:.2f}".format(total_cost))