def city_country(city_name, country_name, population=0):
    """Display nicely formatted city and country with population."""
    if population == 0:
        city_info = f"{city_name.title()}, {country_name.title()}"
    else:
        city_info = f"{city_name.title()}, {country_name.title()} - population {population}"

    return city_info