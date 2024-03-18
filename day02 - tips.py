print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("What percent tip would you like to give? 20, 25, or 30? ")
people = input("How many people will split the bill? ")
bill_as_float = float(bill)
tip_as_int = int(tip)
people_as_int = int(people)
tip_as_percent = tip_as_int / 100
total_tip_amount = bill_as_float * tip_as_percent
total_bill = bill_as_float + total_tip_amount
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
