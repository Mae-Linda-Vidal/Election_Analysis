countries = ["Arapahoe","Denver","Jefferson"]
if countries[1] == 'Denver':
    print(countries[1])

countries = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in countries:
    print("El Paso is in the list of countries.")
else:
    print("El Paso is not the list of countries.")

if "Arapahoe" in countries and "El Paso" in countries:
    print("Arapahoe and El Paso are in the list of countries.")
else:
    print("Arapahoe or El Paso is not in the list of countries.")

if "Arapahoe" in countries or "El Paso" in countries:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in countries and "El Paso" not in countries:
    print("Only Arapahoe is in the list of countries.")
else:
    print("Arapahoe is in the list of countries and El Paso is not in the list of countries.")

for county in countries:
    print(county)

countries_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(countries_tuple)):
    print(countries_tuple[i])

countries_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in countries_dict:
    print(county)

countries_dict.keys() == {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in countries_dict.keys():
    print(county)

countries_dict.values() == {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for voters in countries_dict.values():
    print(voters)

for county in countries_dict:
    print(countries_dict[county])

countries_dict.items() == {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, value in countries_dict.items():
    print(key, value)

countries_dict.items() == {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in countries_dict.items():
     print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
     print(voting_data[i]['county'])
    
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

countries_dict.items() == {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in countries_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in countries_dict.items():
    print(f"{county} county has {voters} registered voters.")




