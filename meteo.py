import requests as req
try:
    from bs4 import BeautifulSoup
except ImportError:
    exit('За да работи, тази програма има нужда от модула Beautiful Soup. Инсталирам с командата : pip install bs4)')

def meteo(city):
    res = req.get(city)
    data = res.content
    html = BeautifulSoup(data, 'html.parser')
    opasni = html.body.find('div', attrs={'class': 'opasnitxt'}).getText()
    tag = html.select('.gradove')
    table = str(tag[0])
    if 'Няма опасност' not in table:
        print(opasni)
    else:
        print('Утре ще бъде спокойно.')

city = input('Сега пиша името на региона, за който да разбера дали ще бъде опасно времето утре :')

def identify(city):
    return {
        "Благоевград": 2303,
        "Бургас": 10,
        "Добрич": 8,
        "Габрово": 2508,
        "Кюстендил": 15,
        "Кърджали": 13,
        "Ловеч": 3,
        "Монтана": 2,
        "Пазарджик": 2321,
        "Перник": 40,
        "Плевен": 4,
        "Пловдив": 12,
        "Разград": 7, 
        "Русе": 6,
        "Шумен": 2310,
        "Силистра": 2311,
        "Сливен": 11,
        "Смолян": 2351,
        "Област София": 2510,
        "София": 14,
        "Търговище": 2399,
        "Велико Търново": 5,
        "Варна": 9,
        "Видин": 1,
        "Враца": 2305,
        "Стара Загора": 2318,
        "Хасково": 2320,
        "Ямбол": 2368
    }[city]

# Актуални данни за различните региони на България от Националния Институт по Метереология и Хидрология
city = f"http://weather.bg/0index.php?koiFail=RM01opasni2&ci={identify(city)}&nd=1&lng=0"

meteo(city)