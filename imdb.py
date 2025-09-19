import requests
from bs4 import BeautifulSoup

def getInfo(film):
	headers = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
	}

	film_name = '-'.join(film.split('-')[:-1])
	# print(film_name)

	content_letterboxd = requests.get(f'https://letterboxd.com/film/{film_name}',headers=headers).text

	soup_letterboxd = BeautifulSoup(content_letterboxd,'lxml')

	film_year = soup_letterboxd.find('span',class_='releasedate').text.strip()

	input_year = film.split('-')[-1]

	# print(film_year,input_year)
	# print(type(film_year),type(input_year))

	if film_year != input_year:
		content_letterboxd = requests.get(f'https://letterboxd.com/film/{film}',headers=headers).text
		soup_letterboxd = BeautifulSoup(content_letterboxd,'lxml')
		print('not equal')

	film_id = soup_letterboxd.find('a',class_='micro-button track-event')['href'].split('/')[-2]

	content_imdb = requests.get(f'https://www.imdb.com/title/{film_id}/parentalguide/',headers=headers).text

	soup_imdb = BeautifulSoup(content_imdb,'lxml')

	section = soup_imdb.find_all('section',class_='ipc-page-section ipc-page-section--base')[1]

	adult_content = section.find_all('div', class_="ipc-list-card--border-line ipc-list-card--base ipc-list-card sc-a25cb019-0 coGWep")

	return adult_content

if __name__== "__main__":
	# print(getInfo('weapons-2025'))
	name = input('name: ')
	name = '-'.join(name.split())
	for part in getInfo(name):
		print('*',part.text)