import random
import requests


#Generate a random Pokemon using the random number
def get_rand_pokemon():

    pokemon_ID = random.randint(1,151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_ID)

    response = requests.get(url)
    get_pokemon = response.json()

    return get_pokemon


# pokemon  = get_rand_pokemon()
# pprint(pokemon)