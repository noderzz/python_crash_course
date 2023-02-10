def city_country(city, country, population=''):
    """Return a single line of 'City, Country'."""
    if population:
        place = f"{city}, {country} - population {population}"
    else:
        place = f"{city}, {country}"
    return place.title()