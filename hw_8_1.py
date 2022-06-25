import requests
url_ = 'https://akabab.github.io/superhero-api/api/all.json'
heroes_list_ = ['Thanos', 'Captain America', 'Hulk']


def get_data(url):
    return requests.get(url=url).json()


def find_smartest_hero(url, heroes_list):
    n, p, i = 'name', 'powerstats', 'intelligence'
    heroes_dict = {hero[n]: hero[p][i] for hero in get_data(url) if hero[n] in heroes_list}
    return max(heroes_dict, key=heroes_dict.get)


if __name__ == '__main__':
    print(find_smartest_hero(url_, heroes_list_))
