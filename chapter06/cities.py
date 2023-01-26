#Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    'tokyo':{'country':'japan','population':'at least 4','fact':'they got anime'},
    'new york':{'country':'usa','population':7,'fact':'they got food'},
    'sao paulo':{'country':'brazil','population':70_000,'fact':'they got snakes'},
}
for city,information in cities.items():
    print(f"{city.title()} is a neat city, here is some info on them:")
    print(f"\tThey are located in {information['country'].title()}.")
    print(f"\tTheir population is {information['population']}.")
    print(f"\tAn interesting fact about them is: {information['fact'].title()}.")