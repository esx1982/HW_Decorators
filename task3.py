# Применить написанный логгер к приложению из любого предыдущего д/з.

import requests
from task2 import logger

@logger('task3.log')
def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    # ваш код здесь
    names = ['Hulk', 'Captain America', 'Thanos']
    response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    max_intelligence = 0
    smartiest_hero = None
    if 200 <= response.status_code <= 300:
        for hero in response.json():
            for name in names:
                if name == hero.get("name"):
                    intelligence = hero.get("powerstats", {}).get("intelligence", 0)
                    if intelligence > max_intelligence:
                        max_intelligence = intelligence
                        the_smartest_superhero = hero.get("name")
    return the_smartest_superhero

if __name__ == '__main__':
    print(get_the_smartest_superhero())