#Program 2 CS 10, Fall 2013 Muntaha Samad
def payment():
    p = eval(input("\nThe amount of the loan: "))
    apr = eval(input("The annual percentage interest rate: "))
    years = eval(input("The number of years of the loan: "))
    max = eval(input("The maximum monthly payment that you can afford: "))
    n = years*12
    apr = apr/100.00
    i = apr/12
    m = (p*i*((1+i)**n))/(((1+i)**n)-1)
    t = (n * m)
    interest = t - p 
    print (p, apr, years, n, i, m)
    print ("\nYour monthly payment will be", m, "dollars.")
    print ("The total amount you will pay is", t, "dollars.")
    print ("The total amount of interest you will pay on a loan of", p, "dollars is", interest, "dollars.")
    if (m <= max):
        print ("Yes, you can afford this loan.\n")
    if (m > max):
        print ("No, you can't afford this loan.\n")

again = eval(input("How many different loans do you want to calculate? "))
for x in range (again):
    print ("\nLoan Calculation Number", x+1)
    payment()
    
print ("Thank you for using our services. Have a nice day.")


    
     
    
