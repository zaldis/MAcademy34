import requests


if __name__ == '__main__':
    print('Do some useful actions')

    response = requests.get('https://google.com')

    print(response.content)
