import time
import sys
import json


def build_info_file(FirstName, LastName, BirthYear, BirthMonth,
                    BirthDay, SpouseName, MarriedYear, KidName,
                    KidBirthYear, PetName, PetType):
    print("Creating list of possible passwords...This may take some time")
    file = open('target_info.txt', 'w')
    file.write(str(FirstName)+"\n")
    file.write(str(FirstName + LastName)+"\n")
    file.write(LastName + FirstName+"\n")
    file.write(LastName + "\n")
    file.write(FirstName + LastName + BirthYear+"\n")
    file.write(FirstName + BirthYear+"\n")
    file.write(LastName + BirthYear+"\n")
    file.write(BirthYear + FirstName + LastName+"\n")
    file.write(FirstName + LastName + BirthDay+"\n")
    file.write(FirstName + LastName + BirthMonth+"\n")
    file.write(FirstName + LastName + BirthDay + BirthMonth + BirthYear+"\n")
    file.write(FirstName + SpouseName+"\n")
    file.write(SpouseName + LastName+"\n")
    file.write(SpouseName + FirstName+"\n")
    file.write(SpouseName+"\n")
    file.write(SpouseName + LastName+"\n")
    file.write(SpouseName + BirthYear+"\n")
    file.write(SpouseName + MarriedYear+"\n")
    file.write(SpouseName + LastName + MarriedYear+"\n")
    file.write(KidName+"\n")
    file.write(KidName + KidBirthYear+"\n")
    file.write(KidBirthYear + KidName+"\n")
    file.write(KidName + LastName+"\n")
    file.write(KidName + LastName + KidBirthYear+"\n")
    file.write(PetName + "\n")
    file.write(PetName + PetType+"\n")
    file.write(PetName + LastName+"\n")
    file.write(PetName + PetType + LastName+"\n")
    file.close
    print("DONE! saved as: target_info.txt")


if (len(sys.argv) < 2):
    print("Targeted Dictionary Attack")
    # Usage Instructions
    time.sleep(1)
    print("\n")
    print("The tool will now ask you a few questions.")
    print("Please answer as many as you can to build the best possible word list")
    print("Unknown answers can be left blank")
    print("")
    time.sleep(1)
    # Basic Target Information
    # This will be the most common information about the target
    FirstName = input("Target's first name: ")
    LastName = input("Target's last name: ")
    BirthYear = input("Target date of birth YEAR: ")
    BirthMonth = input("Target date of birth MONTH: ")
    BirthDay = input("Target data of birth DAY: ")

    married = input("Is the target married? Y , N - ")
    kids = input("Does the target have a kid? Y , N - ")
    pets = input("Does the target have a pet? Y , N - ")

    if married == "Y" or married == "y":
        SpouseName = input("Spouse Name: ")
        MarriedYear = input("What year was the target married on? ")
    else:
        SpouseName = ""
        MarriedYear = ""

    if kids == "Y" or kids == "y":
        KidName = input("Child first name: ")
        KidBirthYear = input("Child year of birth: ")
    else:
        KidName = ""
        KidBirthYear = ""

    if pets == "Y" or pets == "y":
        PetName = input("Pet's name: ")
        PetType = input("What kind of pet? ")
    else:
        PetName = ""
        PetType = ""

    build_info_file(FirstName, LastName, BirthYear, BirthMonth, BirthDay,
                    SpouseName, MarriedYear, KidName, KidBirthYear, PetName, PetType)
else:
    try:
        f = open(sys.argv[1])
        data = json.load(f)
        build_info_file(data['FirstName'], data['LastName'], data['BirthYear'],
                        data['BirthMonth'], data['BirthDay'], data['SpouseName'],
                        data['MarriedYear'], data['KidName'], data['KidBirthYear'],
                        data['PetName'], data['PetType'])
        f.close()
    except:
        print("Error in file handling")
    pass
