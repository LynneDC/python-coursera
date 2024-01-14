# math operator 
print(2 + 4)

# add conditional 
if 2 + 4 < 10:
    print("2 + 4 is less than 10")
else:
    print("2 + 4 is greater than 10")

# use conditional and math operator and logic operator
if 2 + 4 < 10 and 2 + 4 > 5:
    print("2 + 4 is greater than 5 and less than 10")
else:
    print("2 + 4 is not greater than 5 and less than 10")
    
#control flow
# else if statement for a customer to apply the discount on
bill_total = input("What is the total bill?  ")
bill_total = int(bill_total)
if bill_total > 100:
    discount = 0.10
    print("Your discount is {}".format(bill_total * discount))
    print("Your total is {}".format(bill_total - (bill_total * discount)))
elif bill_total > 50:
    discount = 0.05
    print("Your discount is ".format(bill_total * discount))
else:
    discount = 0
    print("You have no discount")