import requests


token = 'secret'

def get_working_list():
    headers = {
        'Authorization': f'Token {token}'
    }
    response = requests.get('https://dvmn.org/api/user_reviews/', headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    print(get_working_list())
