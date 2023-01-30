'''
Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.
'''
def city_country(city, country):
    location = f"{city}, {country}"
    print(location.title())

city_country("tokyo","japan")
city_country("miami","the united states")
city_country("buenos ares","argentina")