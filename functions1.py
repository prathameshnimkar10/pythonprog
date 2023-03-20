bill = float(input('Enter your bill on goods : '))
service_charge = 20

# totaltax = ((bill * service_charge) / 100.00)
# print(totaltax)
# totalbill = totaltax + bill
# print('Your total bill is : ', totalbill)

def calculatetax(bill, service_charge):
    return((bill * service_charge) / 100.00)

print('Total tax =', calculatetax(bill, service_charge))