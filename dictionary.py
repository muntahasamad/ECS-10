def read_set():
    #open and read file
    infile = open("database.txt","r")
    file = infile.readlines()
    
    #make dictionary of IDs
    ID = {}
    ID_list = []
    i = 0
    for line in file:
        (name,ID_number,birthday,major,GPA,hours) = line.split(";")
        
        ID_list.append(name.strip())
        ID_list.append(ID_number.strip())
        ID_list.append(birthday.strip())
        ID_list.append(major.strip())
        ID_list.append(GPA.strip())
        ID_list.append(hours.strip())
        ID_final = ID_number.strip()
        ID[ID_final] = ID_list[i*6:(i*6)+6]
        i=i+1
        
    #make dictionary of names
    Name = {}
    i=0
    for line in file:
        (name,ID_number,birthday,major,GPA,hours) = line.split(";")
        Name[name.strip()] = ', '.join(ID_list[i*6:(i*6)+6])
        i=i+1
        
    #make dictionary of majors
    Major = {}
    for line in file:
        (name,ID_number,birthday,major,GPA,hours) = line.split(";")
        major_final = major.strip()
        ID_final = ID_number.strip()
        if major_final in Major:
                Major[major_final].append(ID_final)
        else:
                Major[major_final] = [ID_final]
                
    #make dictionary of hours            
    Work = {}
    for line in file:
        (name,ID_number,birthday,major,GPA,hours) = line.split(";")
        hours_final = hours.strip()
        ID_final = ID_number.strip()
        if hours_final in Work:
                Work[hours_final].append(ID_final)
        else:
                Work[hours_final] = [ID_final]
                
    return(ID,Name,Major,Work)


def sort_print(ID,name,majors,hours):
    
    #print names alphabetized
    namekeys = name.keys()
    namekeys2 = list(namekeys)
    name_sort = sorted(namekeys2, key=str)
    for item in name_sort:
        info = name[item]
        print(info)
    print()
    
    #print IDs in numerical order    
    IDkeys = ID.keys()
    IDkeys2 = list(IDkeys)
    ID_sort = sorted(IDkeys2, key=int)
    for key in ID_sort:
        info = ID[key]
        info2 = ', '.join(info)
        print (key,":", info2)
    print ()

    #print alphabetized majors and alphabetized students within each major
    namelist = []
    majorkeys = majors.keys()
    majorkeys2 = list(majorkeys)
    major_sort = sorted(majorkeys2, key=str)
    i = 0
    for major in major_sort:
        info = majors[major]
        num = len(info)
        for ids in info:
            info2 = ID[ids]
            names = info2[0]
            namelist.append(names)
            namelist2 = namelist.sort()
            namelist3 = '; '.join(namelist)
        print(major,":", namelist3)
        del namelist[:]

def menu(ID,name,majors,hours):
    print('''\n
    1) Compute the average GPA of all students with a particular major.
    2) Compute the average number of hours worked of all students with a particular major. 
    3) Compute the average GPA of all students who work more than X hours per week.
    ''')
    answer = input("Choose one of the above computations for the program to execute by typing in the corresponding number: ")
    while answer not in ('1','2','3'):
        answer = input("\nChoose one of the above computations for the program to execute by typing in the corresponding number: ")
    if answer == "1":
        average_GPA(majors,ID)
    if answer == "2":
        average_hours_worked(majors,ID)
    if answer == "3":
        GPA_vs_hours(hours,ID)

def average_GPA(majors,ID):
    major2 = ', '.join(majors.keys())
    print ("\n",major2)
    major = input("\nPlease choose which of the above majors you would like to average the GPAs of (capitalize the first letter of each word): ")
    while major not in majors.keys():
         major = input("\nPlease choose which of the above majors you would like to average the GPAs of(capitalize the first letter of each word): ")
    sum = 0
    info = majors[major]
    num = len(info)
    for ids in info:
        info2 = ID[ids]
        GPA = eval(info2[4])
        sum = sum + GPA
        avg = format((sum/num),'.2f')
    print("The average GPA in", major, "is a", avg)
    
def average_hours_worked(majors,ID):
    major2 = ', '.join(majors.keys())
    print ("\n",major2)
    major = input("\nPlease choose which of the above majors you would like to average the hours of work for (capitalize the first letter of each word): ")
    while major not in majors.keys():
         major = input("\nPlease choose which of the above majors you would like to average the hours of work for (capitalize the first letter of each word): ")
    sum = 0
    info = majors[major]
    num = len(info)
    for ids in info:
        info2 = ID[ids]
        GPA = eval(info2[5])
        sum = sum + GPA
        avg = format((sum/num),'.1f')
    print("The average number of hours worked by students in", major, "is", avg,"hours.")
    
def GPA_vs_hours(hours,ID):
    val = True
    while val == True:
        try:
            hoursofwork = int(input("Please specify the minimum number of hours worked you are interested in: "))
            val = False
        
        except:
            print("Please enter a number, not a word")
    sum = 0
    count = 0
    try:
        for item in hours.keys():
            if int(item) > hoursofwork:
                info = hours[item]
                for i in info:
                    info2 = ID[i]
                    GPA = eval(info2[4])
                    sum = sum + GPA
                    count = count + 1
        final = format((sum/count),'.2f')
        print("The average GPA for people who work over", hoursofwork, "hours is: ", final)
    except:
        print("\n Sorry, none of the students in the database have worked that many hours")
                
                
            
        
    
   
#main
        
ID,name,majors,hours = read_set()    
sort_print(ID,name,majors,hours)
while True:
    menu(ID,name,majors,hours)
    answer = input("\nWould you like to make another querie? ").lower()
    while answer not in ("yes","no"):
        print("\nPlease type 'yes' or 'no'")
        answer = input("\nWould you like to make another querie? ").lower()
    if answer == "no":
        print("Goodbye. Have a nice day.")
        break
    
    
    


