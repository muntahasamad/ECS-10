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

def menu():
    print'''1) Compute the average GPA of all students with a particular major.
            2) Compute the average number of hours worked of all students 
            3) Compute the average GPA of all students who work more than X hours per week.'''
    answer = int(input("Choose one of the above computations for the program to execute by typing in the number"))
    while answer not in range(1,4):
        answer = int(input("Choose one of the above computations for the program to execute by typing in the number"))

    #return(answer)
    
    
        
    
   
#main
        
ID,name,majors,hours = read_set()    
sort_print(ID,name,majors,hours)
menu()


