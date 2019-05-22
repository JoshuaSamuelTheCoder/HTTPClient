import requests
import json

def main():
    response = requests.get(
    'https://api.github.com/',
    #params={'q': 'requests+language:python'},
    )

    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    print(json_response['current_user_url'])
    #repository = json_response['items'][0]
    #print(f'Repository name: {repository["name"]}')  # Python 3.6+
    #print(f'Repository description: {repository["description"]}')  # Python 3.6+



if __name__ == '__main__':
    main()
