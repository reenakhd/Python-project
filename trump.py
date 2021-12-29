from pokemon_api import *


#Generate stats dictionary for the random Pokemon(name, id,height,weight + base experience and order)
def get_stat(pokemon):

    stat = {'name': pokemon['name'], 'id': pokemon['id'], 'height': pokemon['height'], 'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience'],'order': pokemon['order']}
    return stat

def pokemonprint(pokemon):#Print pokemon name and stats, create player and opponent print function for clarity
    print('\r\r')
    print('Pokemon stats are:')
    print('Name', '   ', pokemon['name'])
    print('ID', '       ', pokemon['id'])
    print('Height', '   ', pokemon['height'])
    print('Weight', '   ', pokemon['weight'])
    print('Base_experience', '   ', pokemon['base_experience'])
    print('Order', '  ', pokemon['order'])
    print('\r\r')

def run():
    player_pokemon_list = [get_rand_pokemon() for p in range(3)]#player's choice from 3 pokemons

    for i in range(1,4):
        print(i)
        pokemonprint(player_pokemon_list[i-1])

    pokemon_number = int(input('Which Pokemon you like? 1/2/3 '))

    player_pokemon = player_pokemon_list[pokemon_number-1]
    player_pokemon_stat = get_stat(player_pokemon)
    opponent_pokemon = get_rand_pokemon()
    opponent_pokemon_stat = get_stat(opponent_pokemon)

    choice_stat = input('Please select a stat ')#player's stat choice


    pokemonprint(opponent_pokemon)


    if player_pokemon[choice_stat] > opponent_pokemon[choice_stat]:
        print('You win!')
        scorecard['player'] = scorecard['player'] + 1
        print('\r\r')
        print('Player')
        print(scorecard['player'])
        print('Opponent')
        print(scorecard['opponent'])



    elif player_pokemon[choice_stat] < opponent_pokemon[choice_stat]:
        print('You lose!')
        scorecard['opponent'] = scorecard['opponent'] + 1
        print('\r\r')
        print('Player')
        print(scorecard['player'])
        print('Opponent')
        print(scorecard['opponent'])


    else:
        print('It is a draw. Please try again!')

    return

scorecard = {'player': 0, 'opponent': 0}

#Start the game
c = 3#Number of rounds
while c > 0:
    run()
    c = c-1
    print('\r\r\r')
    print('You have {} games left in this session!'.format(c))
    print('\r\r\r\r\r')
if c == 0:
    print('Game over!')
