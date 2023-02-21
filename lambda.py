

people = [{'name': 'Jhon', 'location': 'Ernakulam'},
          {'name': 'Fahiz', 'location': 'Pune'}
          ]

# def f(people):
#    return people['name']

people.sort(key=lambda person:person['name'])
print(people)