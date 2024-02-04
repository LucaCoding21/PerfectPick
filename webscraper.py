
import requests
from bs4 import BeautifulSoup
import json


def get_builds(my_champion):

    url = f'https://www.leagueofgraphs.com/champions/builds/gwen'
    # Send an HTTP request to the website.
    response = requests.get(url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the HTML content of the page.
        soup = BeautifulSoup(response.text, 'html.parser')


        counter_elements = soup.select('img.requireTooltip.item-4633-48')

        #get top 3 champions
        
 
        top_counters = [counter.text.strip() for counter in counter_elements[:3]]
        print(counter_elements)
        return top_counters
    
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def get_top_counters(enemy_champion):
   
    url = f'https://www.counterstats.net/league-of-legends/{enemy_champion}'
    # Send an HTTP request to the website.
    response = requests.get(url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the HTML content of the page.
        soup = BeautifulSoup(response.text, 'html.parser')


        counter_elements = soup.select('span.champion')

        #get top 3 champions
        
 
        top_counters = [counter.text.strip() for counter in counter_elements[:3]]

        return top_counters
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None



def get_counter_info(enemy_champion):
    url2 = f'https://www.championcounter.com/{enemy_champion}'
    
    # Send an HTTP request to the website.
    response = requests.get(url2)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the HTML content of the page.
        soup = BeautifulSoup(response.text, 'html.parser')


        counter_elements = soup.select('li.fadeIn.opened')


        #get top 3 champions
        
 
        top_counters = [counter.text.strip() for counter in counter_elements]
        print(counter_elements)
        return top_counters
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None
    

def create_champion_data():
    # List of champions you want to fetch data for.
    champions = [
    'Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelion-Sol',
    'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', 'ChoGath',
    'Corki', 'Darius', 'Diana', 'Dr-Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks',
    'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim', 'Heimerdinger',
    'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan-IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', 'KaiSa', 'Kalista',
    'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', 'KhaZix', 'Kindred', 'Kled',
    'KogMaw', 'LeBlanc', 'Lee-Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar',
    'Maokai', 'Master-Yi', 'Miss-Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko',
    'Nidalee', 'Nocturne', 'Nunu-Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana',
    'Quinn', 'Rakan', 'Rammus', 'RekSai', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani',
    'Senna', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain',
    'Sylas', 'Syndra', 'Tahm-Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere',
    'Twisted-Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'VelKoz', 'Vi', 'Viktor', 'Vladimir',
    'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'Xin-Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed',
    'Ziggs', 'Zilean', 'Zoe', 'Zyra', 'Samira', 'Seraphine', 'Tell', 'Diego', 'Gwen', 'Anshan', 'Vex', 'Zeri',
    'Renata-Glasc', 'BelVeth', 'Nilah', 'KSante', 'Milio', 'Naafiri'
]

    champion_data = {}
#for every champion in the list get the 
    for champion in champions:
        url = f'https://www.mobafire.com/images/champion/square/{champion}.png'
        
        # get 3 counters 
        #example is [Teemo,Darius,Kayle]
        top_counters = get_top_counters(champion)

        print("succwess")

        champion_data[champion] = {'TopCounters': top_counters,'ChampImg': url}
        # champion_data[champion] = {'TopCounters': top_counters}
        

        
    return champion_data


# create_champion_data()
# def save_to_json(data, file_path):
#     with open(file_path, 'w') as json_file:

#         json.dump(data, json_file, indent=2)

# if __name__ == "__main__":
#     data = create_champion_data()
#     save_to_json(data, 'champion_data.json')
get_builds('gwen')
# get_counter_info('darius')