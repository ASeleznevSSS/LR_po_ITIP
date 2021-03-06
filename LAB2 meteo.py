import requests

def main():
    city = 'Moscow,RU'
    appid = 'fdd9f0e8e0ea402a73e30fb25f49ea2b'
    res = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print('Прогноз погоды на неделю:')
    for i in data['list']:
        print('Дата:',i['dt_txt'],
              '\nТемпература:',i['main']['temp'],'°C'
              '\nПогодные условия:',i['weather'][0]['description'],
              '\nСкорость ветра:',i['wind']['speed'],'м/с'
              '\nВидимость:',i['visibility'],'метров')
        print('____________________________')

if __name__ == '__main__':
    main()
