from json import dumps
from time import sleep

from requests import get

url = "https://api.lolicon.app/setu/v2?r18=1&num=20&size=regular&tag=%E8%90%9D%E8%8E%89|%E5%B0%91%E5%A5%B3"
anu = get(url).json()


def get_lol_pic():
    for x in anu["data"]:
        x["url"] = x["urls"]["regular"].replace("https://i.pixiv.re/", "")
        with open(f"./data/{x['pid']}_{x['p']}.json", "w") as f:
            f.write(dumps(x))


if __name__ == "__main__":
    for x in range(50):
        get_lol_pic()
        sleep(5)
