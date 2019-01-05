import requests
FOOTY_URL = 'http://www.fplstatistics.co.uk/Home/AjaxPricesDHandler?iselRow=-302&_=1546686155618'


def get_football_data():
    """
    Get the football data from the fplstatistics website

    :return: List of football data
    :raises: JSONDecodeError if no JSON found
    :raises: Exception
    """
    request = requests.get(FOOTY_URL)
    raw_data = request.json().get('aaData')
    if raw_data:
        return raw_data
    raise ValueError('It done fucked up')


def get_players_to_sell(players):
    """
    Provides a list of players that, if I have, I should consider selling for money reasons

    :param players: list of players
    :return: list of players
    """
    if not isinstance(players, list):
        raise ValueError('expected list')
    return [player for player in players if player[11] < -100]

def get_player_sell_status()

