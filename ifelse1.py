bill = int(input("Enter bill : "))
discount1 = 50
discount2 = 75

if bill > 200 and bill < 500:
    print("Bill is greater than 200")
    bill = bill - discount1
elif bill > 500:
    print("Bill is greater than 500")
    bill = bill - discount2
else:
    print("Bill is less than 200")

print("Total bill is : " +str(bill))