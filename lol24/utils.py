import time

import pandas as pd
import requests
from tqdm import tqdm

from constants import API_KEY, MATCH_ID_URL


def check_count(cnt: int, start: float):
    if cnt == 99:
        diff = time.time() - start
        if diff < 120:
            time.sleep(round(120 - diff) + 1)
            cnt = 0
            start = time.time()
    else:
        cnt += 1
    return (cnt, start)


def get_user_info(
    rank_list: list = ["CHALLENGER", "GRANDMASTER", "MASTER"],
    level_list: list = ["I", "II", "III", "IV"],
) -> list:
    res = []
    for rank in rank_list:
        for rank_level in level_list:
            i = 1
            while True:
                url = f"https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/{rank}/{rank_level}?page={i}&api_key={API_KEY}"
                req = requests.get(url)
                if req.status_code == 400:
                    break
                print(rank, rank_level, i)
                user = req.json()
                res += user
                time.sleep(1)
                if len(user) == 0:
                    break
                else:
                    i += 1
    return res


def get_puuid(df: pd.DataFrame) -> list:  # df is a dataframe that have user information
    puuid_list = []
    start = time.time()
    cnt = 0
    for id in tqdm(df["summonerId"]):
        url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/{id}?api_key={API_KEY}"
        try:
            puuid = requests.get(url).json()["puuid"]
            cnt, start = check_count(cnt, start)
            puuid_list.append(puuid)
        except:
            puuid_list.append("")
            print(requests.get(url).json())
            cnt, start = check_count(cnt, start)
            pass
    return puuid_list


def get_match_id(df: pd.DataFrame) -> list:
    match_list = []
    start = time.time()
    cnt = 0
    for puuid in tqdm(df["puuid"]):
        url = MATCH_ID_URL.format(puuid=puuid, api_key=API_KEY)
        match_id = requests.get(url).json()
        cnt, start = check_count(cnt, start)
        if len(match_id) != 0:
            match_list.extend(match_id)
    return match_list
