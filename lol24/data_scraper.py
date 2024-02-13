import argparse
import random
import time

import pandas as pd
import requests
from tqdm import tqdm

from constants import API_KEY, MATCH_INFO_URL

# from utils import check_count

parser = argparse.ArgumentParser(description="Enter the three integer")
parser.add_argument(
    "--start",
    "-s",
    type=int,
    required=True,
    help="Enter the start index of data as an integer",
)
parser.add_argument(
    "--end",
    "-e",
    type=int,
    required=True,
    help="Enter the end index of data as an integer",
)
parser.add_argument(
    "--doc_n",
    "-d",
    type=int,
    required=True,
    help="Enter the save file number as an integer",
)


args = parser.parse_args()
match_list = pd.read_csv("match_id.csv")

match_id_list: list = list(match_list["match_id"])
random.shuffle(match_id_list)


match_info_list: list = []
start = time.time()
cnt: int = 0
for match_id in tqdm(match_id_list[args.start : args.end]):
    url = MATCH_INFO_URL.format(match_id=match_id, api_key=API_KEY)
    req = requests.get(url)
    cnt += 1
    if cnt % 500 == 0:
        df = pd.json_normalize(match_info_list)
        df.to_csv(f"match_info_{args.doc_n}.csv", index=False)

    if req.status_code == 200:
        match_info = req.json()
        # cnt, start = check_count(cnt, start)
        match_info_list.append(match_info)

    elif req.status_code == 429:
        while True:  # 429error가 끝날 때까지 무한 루프
            if req.status_code == 429:
                time.sleep(10)
                req = requests.get(url)
            elif req.status_code == 200:  # 다시 response 200이면 loop escape
                match_info_list.append(match_info)
                break
    elif req.status_code == 403:
        print("Your API KEY is expired")
        break
df = pd.json_normalize(match_info_list)
df.to_csv(f"match_info_{args.doc_n}.csv", index=False)
