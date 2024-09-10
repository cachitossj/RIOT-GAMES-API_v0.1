from configparser import ConfigParser
import requests
import pandas as pd
import logging
from typing import Optional, Dict

# Configuración de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Cargamos la configuración
config = ConfigParser()
config.read("C:/Youtube-Projects/riotgames_demoV0/riotgames_demov0/config/config.ini")

# Seteamos los arámetros globales
params = {
    "API_KEY": config["api_riot"]["API_KEY"],
    "player_puuid": config["player_info"]["player_puuid"],
}

# Función para manejar las peticiones HTTP
def make_request(url: str) -> Optional[Dict]:
    """Realiza una petición HTTP y maneja posibles excepciones.

    Args:
        url (str): URL a la cual realizar la petición.

    Returns:
        Optional[Dict]: Diccionario con la respuesta JSON o None en caso de error.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sí el estatus no es 200, lanza un error 
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Se produjo un error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Se produjo un error de conexión: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Se produjo un error de tiempo de espera: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Se produjo un error general: {req_err}")

    return None

# Función para obtener el PUUID
def get_puuid(summonerId: Optional[str] = None,
              gameName: Optional[str] = None,
              tagLine: Optional[str] = None,
              region: str = 'americas') -> Optional[str]:
    """Obtiene el PUUID de un Summoner ID o Riot ID y Tag.

    Args:
        summonerId (Optional[str], optional): ID de invocador. Por defecto None.
        gameName (Optional[str], optional): Nombre de Riot ID. Por defecto None.
        tagLine (Optional[str], optional): Tag de Riot. Por defecto None.
        region (str, optional): Región. Por defecto 'americas'.

    Returns:
        Optional[str]: PUUID del jugador o None si no se encuentra.
    """
    if summonerId is not None:
        url = f'https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{summonerId}?api_key={params["API_KEY"]}'
        logging.info(f"Obteniendo PUUID mediante el ID...")
    else:
        url = f'https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={params["API_KEY"]}'
        logging.info(f"Obteniendo el PUUID del jugador: {gameName}#{tagLine}...")

    response_json = make_request(url)

    if response_json:
     logging.info(f"Se obtuvo el PUUID con éxito!")
     return response_json.get('puuid')
    else: None

# Función para obtener el Riot ID
def get_idtag_from_puuid(puuid: Optional[str]) -> Optional[Dict[str, str]]:
    """Obtiene el Riot ID y Tag a partir de un PUUID.

    Args:
        puuid (Optional[str]): PUUID del jugador.

    Returns:
        Optional[Dict[str, str]]: Diccionario con Riot ID y Tag, o None si no se encuentra.
    """
    if puuid is None:
        logging.warning("No se proporcionó el PUUID para buscar el RIOT ID.")
        return None

    url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={params["API_KEY"]}'
    logging.info(f"Obteniendo Riot ID...")

    response_json = make_request(url)
    if response_json:
        id = {
            'gameName': response_json.get('gameName'),
            'tagLine': response_json.get('tagLine')
        }
        logging.info(f"Riot ID obtenido con éxito!")
        return id
    return None

# Función para obtener la tabla de posiciones
def get_ladder() -> pd.DataFrame:
    """Obtiene la tabla de posiciones (Ladder) de las 3 ligas competitivas más altas.

    Returns:
        pd.DataFrame: DataFrame con los jugadores ordenados por su posición.
    """
    base_url_region = 'https://la2.api.riotgames.com/'
    endpoints = {
        'challengers': 'lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5',
        'grandMasters': 'lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5',
        'masters': 'lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5'
    }

    ladder_dfs = []

    for rank, endpoint in endpoints.items():
        url = f"{base_url_region}{endpoint}?api_key={params['API_KEY']}"
        logging.info(f"Obteniendo datos de la tabla {rank}.")
        response_json = make_request(url)

        if response_json:
            df = pd.DataFrame(response_json['entries'])
            df = df.sort_values('leaguePoints', ascending=False).reset_index(drop=True)
            ladder_dfs.append(df)

    # Concatenamos los DataFrames y realizamos las transformaciones
    if ladder_dfs:
        ladder = pd.concat(ladder_dfs).reset_index(drop=True)
        ladder = ladder.drop(columns='rank').reset_index(drop=False).rename(columns={'index': 'rank'})
        ladder['rank'] += 1  # Ajustar los rangos reales
        logging.info(f"Se obtuvo éxitosamente la tabla de posiciones!")
        return ladder

    logging.error("No se pudieron obtener los datos de la tabla de posiciones.")
    return pd.DataFrame()  # Retorna un DataFrame vacío si hay un error
