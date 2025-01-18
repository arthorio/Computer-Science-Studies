sestelo = {'first_name': 'Lucas', 
           'last_name': 'Sestelo',
           'age': '23',
           'city': 'Toronto'}

roger = {'first_name': 'Roger', 
           'last_name': 'Hiago',
           'age': '23',
           'city': 'BH'}

gabriel = {'first_name': 'Gabriel', 
           'last_name': 'Sousa',
           'age': '24',
           'city': 'Conquista'}

people = [sestelo, roger, gabriel]


favorite_places = {'sestelo': ['home', 
                               'skating park', 
                               'mc donalds'],
                   'roger': ['smoking alley', 'night club'],
                   'gabriel': ['mucuge', 'rivers', 'waterfalls']}

#6-11. Cities:

cities = {'mucuge': {'population' : '12000', 
                     'location': 'chapada diamantina',
                     'weather': 'raining'},
          'salvador': {'population' : '2500000', 
                     'location': 'litoral baiano',
                     'weather': 'crazy'},
          'conquista': {'population' : '400000', 
                     'location': 'sul da bahia',
                     'weather': 'cold and dirty'}}

for cities, information in cities.items():
    print(cities.title())
    for info, values in information.items():
        print("\t" + info + ": " + values)



# .values(), .keys()
