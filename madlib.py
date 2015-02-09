def madlib ():
    
    fileName = input("What is the name of the file where the original text is? ")
    finalName = input ("Where would you like the final text to be printed? ")
    infile = open(fileName, "r")
    data = infile.read()
    # Separating the file into a list of words
    split = data.split()
    Words = []
    for i in data.split():
        Words.append(i)
    # Making a list of the key words
    Keys = []
    for abbrevs in Words:
        if abbrevs[0:2] == "NB":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "NS":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "NP":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "AJ":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "AV":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "NM":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "VB":
            Keys.append (abbrevs)
        if abbrevs[0:2] == "VP":
            Keys.append (abbrevs)
        else:
            ()
    print (Keys)

            
    New_Keys = []

    # Asking the user to input words
    #if and elif used to deal with punctuation
    
    for items in Keys:
        if items[0:2] == "NB":
            word = input("Please input a number ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)
                
        if items[0:2] == "NS":
            word = input("Please input a singular noun ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)
                
        if items[0:2] == "NP":
            word = input("Please input a plural noun ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)
                
        if items[0:2] == "AJ":
            word = input("Please input an adjective ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)
                
        if items[0:2] == "AV":
            word = input("Please input an adverb ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)

        if items[0:2] == "NM":
            word = input("Please input a person's name ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)

        if items[0:2] == "VB":
            word = input("Please input a verb ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)

        if items[0:2] == "VP":
            word = input("Please input a past-tense verb ")
            if items [-1] == ",":
                word = word+","
                New_Keys.append (word)
            elif items [-1] == ".":
                word = word + "."
                New_Keys.append (word)
            else:
                New_Keys.append (word)
    print (New_Keys)

    # Adding the inputted words into the story 
    final_story = []
    p=0
    for val in Words :
        if val [0:2] == "NB":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1
            
        elif val [0:2] == "NS":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1

        elif val [0:2] == "NP":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1

        elif val [0:2] == "AJ":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1

        elif val [0:2] == "AV":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1

        elif val [0:2] == "NM":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1

        elif val [0:2] == "VB":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1

        elif val [0:2] == "VP":
            addword = New_Keys [p]
            final_story.append (addword)
            p = p+1
            
        else:
            final_story.append(val)
            
    #converting the story from a list to a string and ensuring there are spaces between each word
            
    
    str1= " ".join(final_story)
    print ("\nThe Madlib Story\n", str1)
    outfile = open(finalName, "w")
    outfile.write (str1)
            
    

madlib()
    

    
