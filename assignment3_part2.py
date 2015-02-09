#Assignment 3 part 2 Muntaha Samad ECS10


def Easter ():

    year = eval(input("Input a year to find out the day of Easter "))
    if (year >= 1900 and year <= 2099):
        
        a = year % 19
        b = year % 4
        c = year % 7
        d = ((19*a)+24) % 30
        e = ((2*b) + (4*c) + (6*d) + 5) % 7
        eDay = 22 + (d + e)
        
        YEARS = [1954, 1981, 2049, 2076]
        if (year in YEARS):
            eDay = eDay - 7
        if (eDay > 31):
            eDay = eDay - 31
            print ("In the year", year, "Easter fell on April the", eDay)
        elif (eDay <= 31):
            print ("In the year", year, "Easter fell on April the", eDay)
    else:
        print ("Invalid input for the year")
        

Easter ()            
            
        
