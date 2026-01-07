from city_functions import city_country

def test_city_country():
    """Do city and country like Santiago, Chile work?"""
    city_country_string = city_country('santiago','chile')
    assert city_country_string == "Santiago, Chile"

def test_city_country_population():
    """Do city and country like Santiago, Chile - population 5000000 work?"""
    city_country_string = city_country('santiago','chile', 5000000)
    assert city_country_string == "Santiago, Chile - population 5000000"