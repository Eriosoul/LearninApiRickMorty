import os
import requests
from requests import Response
from data_class.api_result import APIResults, APIInfoData
from dotenv import load_dotenv


class RickMortyAPI:
    def __init__(self):
        load_dotenv()
        self.url_info: str = os.getenv('URL_INFO')
        self.url_char: str = os.getenv('URL_CHAR')

    def get_info(self) -> APIInfoData:
        try:
            r: Response = requests.get(self.url_info)
            if r.status_code != 200:
                return APIInfoData(count=0, pages=0, next="", prev="")
            content: dict = r.json()
            # I get all the json info, I get the index from all array
            info: dict = content.get("info")
            count: int = info.get("count")
            pages: int = info.get("count")
            next_page: str = info.get("next")
            previous: str = info.get("prev")
            # we return all the info what we got
            print(APIInfoData(count=count, pages=pages, next=next_page, prev=previous))
            return APIInfoData(count=count, pages=pages, next=next_page, prev=previous)
        except requests.RequestException as e:
            # we catch the error if we don't get any info
            print('An error has ocurred ', {e})
            return APIInfoData(count=0, pages=0, next="", prev="")

    def get_character_info(self) -> APIResults:
        character_id = 1
        try:
            r: Response = requests.get(self.url_char + '/' + str(character_id))
            if r.status_code != 200:
                print('Errors')
                return APIResults(id=0, name="", species="", status="", image="")
            content: dict = r.json()
            id_char: int = content.get("id")
            name: str = content.get("name")
            species: str = content.get("species")
            status_char: str = content.get("status")
            img: str = content.get("image")
            return APIResults(id=id_char, name=name, species=species, status=status_char, image=img)
        except requests.RequestException as e:
            print("Imposible to get data", {e})
            return APIResults(id=0, name="", species="", status="", image="")

    def get_episodes(self):
        print('pepe')
