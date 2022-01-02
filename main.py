import requests, bs4
url = 'https://anekdot.ru/random/anekdot'                        
h   = {"User-Agent":"1"}                   # сайт не пускает без header
web = requests.get(url, headers=h).text    # Получение кода веб-сайта, где расположены случайные анекдоты

bs      = bs4.BeautifulSoup(web, "lxml")                             
text    = str(bs.find_all(class_="topicbox")[1].find(class_="text"))  # получаем элемент, в котором написан текст анекдота
anekdot = text[26:-6].replace("<br/>","\n")                           # удаляем лишние теги, которые попали в наш текст. заменяем тег переноса на \n

print(f"\n{anekdot}\n")
