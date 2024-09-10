from main import *

if __name__ == "__main__":

    get_puuid(summonerId=params['player_puuid'],
        gameName='Hachi', tagLine='LAS', region='americas')

    get_idtag_from_puuid(params['player_puuid'])

    get_ladder()
