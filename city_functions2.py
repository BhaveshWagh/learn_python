def city_country_information2(city_name, country_name,population = 0):
    city_country_name = f"{city_name}, {country_name}"
    if population:
        city_country_name += f" {population}"
    return city_country_name.title()

