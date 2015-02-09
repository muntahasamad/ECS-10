#Assignment3 part 1 Muntaha Samad ECS10
def DayNum ():
    
    month = input("Input a month. Spell  it out completely, and capitalize the first letter ")    
    day = input("Input a day ")
    year = input("Input a year ")
     
    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    foundit = 0
    
    for i in range(12):
            
        if (MONTHS[i] == month):
            foundit = 1
            monthNum = i + 1
            
    if (foundit == 1):
         
         

        #determine if the year is a century year
        if (year[-1] == '0' and year[-2] == '0'):
            century = 1
        else:
            century = 0

        #convert the strings "year" and "day" to integers, so we can do arithmetic on them.
        year = eval(year)
        day = eval(day)

        #determine if the year is a leap year
        if (century == 1) and ((year % 400) != 0):
            leapyear = 0
        else:
            if ((year % 4) == 0):
                leapyear = 1
                    
            else:
                leapyear = 0
        
        #determine if the date is a valid day

        #first take care of the special case of February
        if  (month == 'February'):
            if (day < 29):
                valid = 1
            else:
                if  (day == 29):
                    if (leapyear == 1):
                        valid = 1
                    else:
                        valid = 0
                else:
                    valid = 0
        
        #next take care of all the other months


        else:
            if (day < 31):
                valid = 1
            else:
                if ((day == 31) and ((month == "January") or (month == "March") or (month == "May") or (month == "July") or (month == "August") or (month == "October") or (month == "December"))):
                    valid = 1

                else:
                    valid = 0
                
        if (valid == 1):
                
            num = 31*(monthNum - 1) + day
            if (monthNum > 2):
                if (leapyear == 1):
                    num = num + 1
                    print ("The day number is",num,".")
                else:
                    num = num - ((4*(monthNum) + 23)//10)
                    print ("The day number is",num,".")
            else:
                    print ("The day number is",num,".")
                    
        else:
            print (month, day, year , "is not a valid date")
               
    elif (foundit == 0):
        print ("This is not a valid month")

DayNum ()
            
