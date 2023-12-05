from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    cafedry_list = soup.select('div#pagecontent ul li a')
    # Создаем список кафедр
    cafedry_names = []
    for cafedry in cafedry_list:
        cafedry_names.append(cafedry.get_text(strip=True))
    save_result_in_file(cafedry_names)


# Функция для сохранения результата в текстовый файл
def save_result_in_file(cafedry_names):
    with open('cafedry_names.txt', 'w') as file:
        for name in cafedry_names:
            file.write(name + '\n')
    file.close()
