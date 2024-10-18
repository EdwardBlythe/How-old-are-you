def printinterest(ir, years, deposit):
    for i in range(years + 1):
        print("Year ", i, " the money will be ", deposit)
        deposit = deposit * ((ir/100) + 1)
def finddouble(ir, deposit):
    compounddeposit = deposit
    years = 0
    while compounddeposit < (deposit * 2):
        compounddeposit = compounddeposit * ((ir/100) + 1)
        years = years + 1
    return years

deposit = int(input("enter deposit"))
ir = float(input("enter interest rate"))
years = int(input("enter number of years you want to save"))
printinterest(ir, years, deposit)
years = finddouble(ir, deposit)
print ("To double would take ", years, " years")




        

