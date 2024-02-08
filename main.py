import questionary
import requests
from models import streamwish,filelions
import subprocess
API_BASE_URL = ""
def fetch(param:str,url:str):
    req = requests.get(f'{url}{param}')
    try:
        if req.status_code == 200:
            return req.json()
        else:
            return None
    except:
        return None
def main():
    print('cool-anime-cli ready 🥳')
    QUERY = questionary.text("Enter Anime Name").ask()
    print(f'fetching results for {QUERY}')
    search_results = fetch(QUERY,"https://api.anime-dex.workers.dev/search/")
    if search_results == None:return None

    selected_anime = questionary.select(
        "Select the anime",
        choices=[f"{item['title']} - {item['id']} - ({item['releaseDate'].split(' ')[-1]})" for item in search_results['results']],
    ).ask()
    
    anime_results = fetch(selected_anime.split('-')[-2],"https://api.anime-dex.workers.dev/anime/")
    print("> Name : ",anime_results['results']['name'])
    print("> Date : ",anime_results['results']['released'])
    print("> Status : ",anime_results['results']['status'])

    selected_episode = questionary.select(
        "Select the episode",
        choices=[f"{item[0]} - {item[1]}" for item in anime_results['results']['episodes']],
    ).ask()
    episode_results = fetch(selected_episode.split(' - ')[-1],'https://api.anime-dex.workers.dev/episode/')
    return [
        {'name':'gogo-1','url':episode_results['results']['stream']['sources'][0]['file']},
        {'name':'gogo-2','url':episode_results['results']['stream']['sources_bk'][0]['file']},
        {'name':'streamwish','url':streamwish(episode_results['results']['servers']['streamwish']) if episode_results['results']['servers']['streamwish'] else None},
        {'name':'filelions','url':filelions(episode_results['results']['servers']['filelions']) if episode_results['results']['servers']['filelions'] else None}
    ]
if __name__=="__main__":
    streams = main()
    selected_server = questionary.select(
        "Select a server",
        choices=[f"{item['name']} - {item['url']}" for item in streams],
    ).ask()
    print('Playing on mpv ...')
    command = ["mpv", selected_server.split(' - ')[-1]]
    subprocess.run(command)
