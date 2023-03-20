loyaltyprogram = bool(input("Are you a part of the loyalty program?"))
bill = float(input("Enter bill : "))

if loyaltyprogram == True and bill > 250:
    print("Thank you for being a loyal customer, enjoy the 40percent discount!")
    totalbill = bill - (float((bill/100) * 40))

elif bill > 250:
    print("Enjoy a 15percent discount!")
    totalbill = bill - (float((bill/100) * 15))

else:
    print("Service charge applied.")
    totalbill = bill + (float((bill/100) * 5))

print("Total bill is : " +str(totalbill))