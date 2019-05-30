def monthlyPaymentPlan(principal, interest, year):
    paymentplan = int((1+interest/(12*100))**(12*year)*principal*(interest/(12*100))/((1+interest/(12*100))**(year*12)-1))
    return paymentplan
print(monthlyPaymentPlan(10000000, 2.8, 4))
