import os
import requests
from requests import Response
from api import api_petition
from dotenv import load_dotenv


class RickMorty:
    def __init__(self):
        self.r = None
        load_dotenv()
        # I will not show the link
        self.url = os.getenv('URL_INFO')

    def get_check_conection(self):
        try:
            self.r: Response = requests.get(self.url)
            if self.r.status_code == 200:
                print('Conection successful')
                return True
        except Exception as e:
            print(f'Error {e}')
            return False

    def get_info_from_web(self):
        if self.get_check_conection():
            response_json: dict = self.r.json()
            options: list = list(response_json.keys())
            print("Options:")
            for index, option in enumerate(options, 1):
                print(index, option)
        else:
            print("Connection is not satisfactory. Unable to proceed with further operations.")

    def get_option_select(self):
        option: str = input('Select an option: ')
        option_index: int = int(option) - 1
        if self.get_check_conection():
            response_json: dict = self.r.json()
            options = list(response_json.keys())

            if 0 <= option_index < len(options):
                selected_option = options[option_index]
                selected_option_link = response_json[selected_option]
                print("Selected option link:", selected_option_link)
                # Llamar a la clase correspondiente en el módulo 'api'
                if selected_option == 'info':
                    characters_instance = api_petition.RickMortyAPI()
                    characters_instance.get_character_info()
                elif selected_option == 'episodes':
                    episodes_instance = api_petition.RickMortyAPI()
                    episodes_instance.get_episodes()
                elif selected_option == 'locations':
                    locations_instance = api_petition.RickMortyAPI()
                    locations_instance.get_info()
            else:
                print("Invalid option index.")
        else:
            print("Connection is not satisfactory. Unable to proceed with further operations.")


if __name__ == '__main__':
    rick: RickMorty = RickMorty()
    rick.get_info_from_web()
    rick.get_option_select()
