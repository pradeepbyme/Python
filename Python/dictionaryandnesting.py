travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stubbgourt"]
    }
]


def add_new_country(country_name, visit_count, city_names):
    dicts = {"country": country_name, "visits": visit_count, "cities": city_names}
    return dicts


dictret = add_new_country("Spain", 13,
                          ["Markando", "Mullistha", "Kakutani"])

travel_log.append(dictret)

for i in range(0, len(travel_log)):
    for item in travel_log[i].items():
        print(item)
    print()


