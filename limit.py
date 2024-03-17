def limit(cardtypes):
        if cardtypes=="1" or cardtypes=="Rupay":
            return 2000
        elif cardtypes=="2" or  cardtypes == "Visa":
            return 5000
        elif cardtypes=="3" or cardtypes== "MasterCard":
            return 10000
        else:
            return 0
