import requests, bs4
def get():
    url = 'https://anekdot.ru/random/anekdot'                        
    h   = {"User-Agent":"1"}                   # сайт не пускает без header
    web = requests.get(url, headers=h).text    # Получение кода веб-сайта, где расположены случайные анекдоты

    bs      = bs4.BeautifulSoup(web, "lxml")                             
    result    = str(bs.find_all(class_="topicbox")[1].find(class_="text"))  # получаем элемент, в котором написан текст анекдота
    text = result.replace("<br/>","\n")                           # удаляем лишние теги, которые попали в наш текст. заменяем тег переноса на \n
    text = text.split(">")
    text[0] = ""
    text = ''.join(text)
    text = text.split("<")
    text[-1] = ""
    text = ''.join(text)
    return text

