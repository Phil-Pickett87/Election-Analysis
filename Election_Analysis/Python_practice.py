print("Hello Wolrd")
type(3)
ballots=1341
type(ballots)
type(73.81)
type("Hello World")
type(True)
type (5+2)*4
counties = ["Arapahoe","Denver","Jefferson"]
counties[0]
print (counties[2])
print (counties[-1])
len(counties)
counties[0:2]
counties[1:]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties.insert(2,"Denver") and counties.insert(1,"Jefferson") and counties.append("Arapahoe")
counties.
my_tuple=tuple
counties_tuple=("Arapahoe","Denver","Jefferson")
len(counties_tuple)
counties_tuple[1]
counties_tuple[:2]
counties_tuple[1:2]
counties_tuple[:-1]
my_dictionary={}
counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
len(counties_dict)
counties_dict.keys()
counties_dict.values()
counties_dict.get("Arapahoe")
counties_dict["Denver"]
voting_data=[]

voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data.insert(1,({"county":"El Paso","registered_voters":461149}))
voting_data.remove({"county":"Arapahoe","registered_voters":422829})
voting_data
counties = ["Arapaho","Denver","Jefferson"]
if counties[1]=='Denver'
 print(counties[1])
 temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
            

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
