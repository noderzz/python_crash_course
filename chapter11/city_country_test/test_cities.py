"""
Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a module called city_functions.py, and save this file in a new folder so pytest won’t try to run the tests we’ve already written.

Create a file called test_cities.py that tests the function you just wrote. Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. Run the test, and make sure test_city_country() passes.
"""
from city_functions import city_country

def test_city_country():
    """Test if normal city/country combinations work."""
    formatted_string = city_country('santiago', 'chile')
    assert formatted_string == "Santiago, Chile"

def test_city_country_population():
    """Test a string with a population."""
    formatted_string = city_country('santiago', 'chile', 5000000)
    assert formatted_string == "Santiago, Chile - Population 5000000"

