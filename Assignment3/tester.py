import univRanking




def removeSpaces(text):
    text = text.replace(" ","")
    text = text.replace("\t","")
    for i in range(100):
        text = text.replace("\n\n","\n")
    return text

def equalWithoutSpaces (expected, student):
    expected = expected.replace(" ", "")
    expected = expected.replace("\t", "")
    student = student.replace(" ", "")
    student = student.replace("\t", "")
    return expected == student

def printLabel(num):
    list =[
        "",
        "# 1 - Universities count",
        "# 2 - Available countries",
        "# 3 - Available continents",
        "# 4 - The university with top international rank",
        "# 5 - The university with top national rank",
        "# 6 - The average score",
        "# 7 - The relative score",
        "# 8 - The capital city",
        "# 9 - The universities that hold the capital name",
    ]
    print("Testing....",list[num],end="....")

def success():
    print("successful!")
def fail():
    print("failed xxxx")



# selectedCountry = input("Please enter the country name:")
selectedCountry ='USA'
univRanking.getInformation(selectedCountry, "TopUni.csv", "capitals.csv")


f= open("output.txt", "r", encoding='utf8')
information = f.read()
f.close()

print("#"* 30+"\nselectedCountry ='USA'\nThe content of output.txt is:\n"+"#"* 30)
print(information)
information = removeSpaces(information)
information = information.upper()
# print(information)

print("\n"+"#"* 30+"\nTesting information about USA:\n"+"#"* 30)

printLabel(1)
if "=>100" in information:
    success()
else:
    fail()

printLabel(2)
if "CANADA" in information and "SWEDEN" in information and "SINGAPORE" in information and "," in information:
    success()
else:
    fail()

printLabel(3)
if "AVAILABLECONTINENTS=>" in information and "NORTHAMERICA" in information and "EUROPE" in information and "AUSTRALIA" in information:
    success()
else:
    fail()

printLabel(4)
if "ATINTERNATIONALRANK=>1THEUNIVERSITYNAMEIS=>HARVARDUNIVERSITY" in information:
   success()
else:
    fail()

printLabel(5)
if "ATNATIONALRANK=>1THEUNIVERSITYNAMEIS=>HARVARDUNIVERSITY" in information:
   success()
else:
    fail()

printLabel(6)
if "=>86.5" in information or "=>86.6" in information:
   success()
else:
    fail()

printLabel(7)
if "INNORTHAMERICAIS=>" in information and "=86.5" in information:
   success()
else:
    fail()

printLabel(8)
if "THECAPITALIS=>WASHINGTON" in information:
   success()
else:
    fail()

printLabel(9)
if "#1" in information and "#2" in information and "UNIVERSITYOFWASHINGTON" in information and "WASHINGTONUNIVERSITY" in information:
   success()
else:
    fail()





selectedCountry ='south korea'
univRanking.getInformation(selectedCountry, "TopUni.csv", "capitals.csv")


f= open("output.txt", "r", encoding='utf8')
information = f.read()
f.close()

print("\n\n"+"#"* 30+"\nselectedCountry ='South Korea'\nThe content of output.txt is:\n"+"#"* 30)
print(information)
information = removeSpaces(information)
information = information.upper()
# print(information)


print("\n"+"#"* 30+"\nTesting information about South Korea:\n"+"#"* 30)


printLabel(1)
if "=>100" in information:
    success()
else:
    fail()

printLabel(2)
if "CANADA" in information and "SWEDEN" in information and "SINGAPORE" in information and "," in information:
    success()
else:
    fail()

printLabel(3)
if "AVAILABLECONTINENTS=>" in information and "NORTHAMERICA" in information and "EUROPE" in information and "AUSTRALIA" in information:
    success()
else:
    fail()

printLabel(4)
if "ATINTERNATIONALRANK=>31THEUNIVERSITYNAMEIS=>SEOULNATIONALUNIVERSITY" in information:
   success()
else:
    fail()

printLabel(5)
if "ATNATIONALRANK=>1THEUNIVERSITYNAMEIS=>SEOULNATIONALUNIVERSITY" in information:
   success()
else:
    fail()

printLabel(6)
if "=>86.5" in information or "=>86.6" in information:
   success()
else:
    fail()

printLabel(7)
if "INASIAIS=>" in information and "=96.3" in information:
   success()
else:
    fail()

printLabel(8)
if "THECAPITALIS=>SEOUL" in information:
   success()
else:
    fail()

printLabel(9)
if "#1" in information and "SEOULNATIONALUNIVERSITY" in information:
   success()
else:
    fail()






selectedCountry ='japan'
univRanking.getInformation(selectedCountry, "TopUni.csv", "capitals.csv")


f= open("output.txt", "r", encoding='utf8')
information = f.read()
f.close()

print("\n\n"+"#"* 30+"\nselectedCountry ='japan'\nThe content of output.txt is:\n"+"#"* 30)
print(information)
information = removeSpaces(information)
information = information.upper()
# print(information)


print("\n"+"#"* 30+"\nTesting information about Japan:\n"+"#"* 30)


printLabel(1)
if "=>100" in information:
    success()
else:
    fail()

printLabel(2)
if "CANADA" in information and "SWEDEN" in information and "SINGAPORE" in information and "," in information:
    success()
else:
    fail()

printLabel(3)
if "AVAILABLECONTINENTS=>" in information and "NORTHAMERICA" in information and "EUROPE" in information and "AUSTRALIA" in information:
    success()
else:
    fail()

printLabel(4)
if "ATINTERNATIONALRANK=>13THEUNIVERSITYNAMEIS=>UNIVERSITYOFTOKYO" in information:
   success()
else:
    fail()

printLabel(5)
if "ATNATIONALRANK=>1THEUNIVERSITYNAMEIS=>KYOTOUNIVERSITY" in information:
   success()
else:
    fail()

printLabel(6)
if "=>85.3" in information or "=>85.4" in information:
   success()
else:
    fail()

printLabel(7)
if "INASIAIS=>" in information and "=95.0" in information:
   success()
else:
    fail()

printLabel(8)
if "THECAPITALIS=>TOKYO" in information:
   success()
else:
    fail()

printLabel(9)
if "#1" in information and "UNIVERSITYOFTOKYO" in information:
   success()
else:
    fail()