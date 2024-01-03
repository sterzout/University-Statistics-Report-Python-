selectedCountry = "usa"
def getInformation(selectedCountry, uniFileName, capFileName):
    output = open("output.txt",'w',encoding='utf8') #opens an output file with the encoding


    try: # opens the files provided with the assignment and reads
        university = open(uniFileName,"r")
        capitals = open(capFileName,"r")
    except IOError: # incase files are not found, exception handling is here
        output.write("File was not found")
        quit()

    def dictionaries(capitals, university): # function to make the capitals dictionary and the school dictionary
        line1 = capitals.readline() # reads the very first line of capitals file
        line1 = capitals.readline() # reads again but onto the next line
        cdict = {} # this is where the capital dictionary information is stored.
        while line1 != "": # runs any line that is not empty
            line1 = line1.strip() # strips the unnecessary last item in the line
            line1 = line1.split(",") # turns each line into a list by separating them with commas


            cdict[line1[0].upper()] = {"Capital": line1[1], "Country Name": line1[0], "Continent": line1[5]}
            # cdict stores the capital dictionary under the capital title by taking index[0] of the very first line
            #(this is why we had readline twice.

            line1 = capitals.readline() # since this is a while loop it uses this readline to access the next line in
            # the file.

        udict = {} # university dictionary is stored here
        line2 = university.readline() # reads the very first line of the TopUni file
        line2 = university.readline() # reads again but onto the next line

        while line2 != "": # this while loop keeps going until it reaches a line with no content
            line2 = line2.strip()
            line2 = line2.split(',')
            udict[line2[1].upper()] = {"Country": line2[2], "World Rank": line2[0], "National Rank":
                         line2[3], "Score": line2[8]}

            line2 = university.readline()
            # this is the same principle as the first dictionary except it stores the University name as a the key instead.
        return [cdict, udict] # returns both dictionaries that were just created.

    dictionaries = dictionaries(capitals, university) # we make a variable called dictionary that contains both
    # in a list so that when we call them its easier by using their indexes just like below.

    udict = dictionaries[1]
    cdict = dictionaries[0]
    # dictionaries are stored as list indexes.

    amtOfSchools = len(udict)
    # returns the number of schools by counting every line except the first one which can be done by counting the
    # length of the university dictionary.
    output.write(f"Amount of schools => {amtOfSchools}\n")
    # outputs the lenght of schools to the output file
    def availableCountriesContinents(udict,cdict):
        availableCTList = [] # list for available Countries
        availableCNList= [] # list for available continents matching the countries
        for key in udict:
            if udict[key]["Country"].upper() not in availableCTList:
                availableCTList.append(udict[key]["Country"].upper())
        # for loop checks if the country is not in the list, then it would be appended to our available countries list.
        output.write(f"Available Countries=> {', '.join(availableCTList)}\n")
        # outputs a formatted list of available countries
        for key in cdict:
            if cdict[key]["Country Name"].upper() in availableCTList:
                if cdict[key]["Continent"].upper() not in availableCNList:
                    availableCNList.append(cdict[key]["Continent"].upper())
        # for loop checks through each line to see if the country name matches one in the available countries list
        # if this is the case it will then check for the continents and see if they are in the continents list already
        # if not it will add the continents that match the countries into our available list
        availableCNList = str(availableCNList).replace("'","").replace("[","").replace("]","")
        # variable cleans up the list to take out quotations and brackets
        output.write(f"Available Continents=> {availableCNList}\n")
        # outputs our available continents list.
        return [availableCNList, availableCTList]
    # returns both available country and continents list.

    bothLists = availableCountriesContinents(udict, cdict)
    availableCTList = bothLists[1]
    availableCNList = bothLists[0]
# returns both available lists to a list containing both with indexes.


    def Question4(CTList, SelectedCountry):

        highestRank = 100
        # we set the highest rank to 100 so that it keeps running until it hits the lowest one since all of them
        # are lower than 100
        schoolName = ''
        # schoolName variable to be filled in the for loop.
        if SelectedCountry.upper() in CTList:
        # this checks to see if the country is in the available countries list
            for key in udict:
                if udict[key]["Country"].upper() == SelectedCountry.upper():
                    # checks each line to see if it matches selected country
                    if int(udict[key]["World Rank"]) < highestRank:
                        highestRank = int(udict[key]["World Rank"])
                        schoolName = key.upper()
        # goes through and sees if their world ranks are lower than highestRank (100) then prints the lowest which
        # in this case would be the best school since the lower, the better ranking.

        output.write(f"At international rank => {highestRank} the university name is => {schoolName}\n")
        # outputs the highest internationally ranked school in that selected country
    Question4(bothLists[1], selectedCountry)
    # function uses available countries lists and the selected country.

    def Question5(CTList,SelectedCountry):
        highestRank = 100
        schoolName = ''
        if SelectedCountry.upper() in CTList:
            for key in udict:
                if udict[key]["Country"].upper() == SelectedCountry.upper():
                    if int(udict[key]["National Rank"]) < highestRank:
                        highestRank = int(udict[key]["National Rank"])
                        schoolName = key.upper()

        output.write(f"At national rank => {highestRank}  the university name is => {schoolName}\n")
    Question5(bothLists[1],selectedCountry)
# does the same as the function above but this time we use the 'National Rank' to output the highest nationally ranked
# school in the given country
    def Question678(CTList,CNList, SelectedCountry):
        sumScore = 0
        sumSchools = 0
        # sumScore is for the score of the school
        # sumSchools is for the school count
        if SelectedCountry.upper() in CTList:
            for key in udict:
                if udict[key]["Country"].upper() == SelectedCountry.upper():
                    sumScore += float(udict[key]["Score"])
                    sumSchools += 1
        # if the selected country matches our criteria it collects all the scores of schools in that country and counts
        # the number of schools as well with the variables above.
        averageScore = sumScore/sumSchools
        # divides total school by number of schools to see average score.
        output.write(f"The average score =>{averageScore: .2f}%\n")
        # outputs the average score value
        highestScore = 0
        # this is 0 for the next for loop to store highestScore
        SCContinent = cdict[SelectedCountry.upper()]["Continent"]
        # our selected continent is the one where our selected country lies in
        for key in udict:
            if cdict[udict[key]["Country"].upper()]["Continent"] ==SCContinent:
                # this runs through each line to see if the country has our selected continent
                if highestScore < float(udict[key]["Score"]):
                    highestScore = float(udict[key]["Score"])
                    # once the selected continent is checked it will take the highest score of all the countries
                    # in our continent

        rScore = (averageScore)/(highestScore) * 100
        # relative score takes the average score and divides it by the highest score of all values in our continent
        output.write(f"The relative score to the top university in {SCContinent.upper()} is "
                     f"=> ({averageScore}) / {highestScore}) x 100% = {rScore}% \n")
        # outputs our values
        output.write(f"The capital is => {(cdict[SelectedCountry.upper()]['Capital']).upper()}\n")
        # outputs the capital of our selected country
    Question678(bothLists[1],bothLists[0], selectedCountry)
    # in this function we used both lists and our selected country
    def Question9(SelectedCountry):
        counter = 1
        # we need a counter for each run in the for loop.
        output.write(f"The university that contain the capital name=>\n")
        for key in udict:
            if udict[key]["Country"].upper() == SelectedCountry.upper():
                if cdict[udict[key]["Country"].upper()]["Capital"].upper() in key.upper():
                    # checks to see if school has the capital in its title

                    output.write(f"#{counter} {key.upper()}\n")
                    counter += 1
                    # this outputs each school with the counter running through to check

    Question9(selectedCountry)
    output.close()
    capitals.close()
    university.close()
    # closing all the files
getInformation(selectedCountry, "TopUni.csv", "capitals.csv")
# using the getInformation function as listed in the assignment with our files and selected countries as the parameters.
