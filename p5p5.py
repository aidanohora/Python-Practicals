town = input("Enter a town or city in Ireland: ")

if town == "Dublin" or town == "dublin":
    print("You entered Dublin. Dublin is in Leinster.")

elif town == "Belfast" or town ==  "belfast":
    print("You have entered Belfast. Belfast is in Ulster.")

elif town == "Cork" or town ==  "cork":
    print("You have entered Cork. Cork is in Munster.")

elif town == "Limerick" or town ==  "limerick":
    print("You have entered Limerick. Limerick is in Munster.")

elif town == "Derry" or town ==  "derry":
    print("You have entered Derry. Derry is in Ulster.")

elif town == "Galway" or town ==  "galway":
    print("You have entered Galway. Galway is in Connacht.")

elif town == "Lisburn" or town == "lisburn":
    print("You have entered Lisburn. Lisburn is in Ulster.")

elif town == "Kilkenny" or town == "kilkenny":
    print("You have entered Kilkenny. Kilkenny is in Leinster.")

elif town == "Waterford" or town == "waterford":
    print("You have entered Waterford. Waterford is in Munster.")

elif town == "Sligo" or town ==  "sligo":
    print("You have entered Sligo. Sligo is in Munster.")

else:
    print("Sorry, I didn't recognise that name.")
