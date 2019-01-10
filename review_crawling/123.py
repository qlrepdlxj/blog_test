import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import pandas as pd

def get_data(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    score_result = html.find('div', {'class': 'score_result'})
    lis = score_result.findAll('li')
    for li in lis:
        nickname = li.findAll('a')[0].find('span').getText()
        created_at = datetime.strptime(li.find('dt').findAll('em')[-1].getText(), "%Y.%m.%d %H:%M")
        review_text = li.find('p').getText()
        score = li.find('em').getText()
        btn_likes = li.find('div', {'class': 'btn_area'}).findAll('span')
        like = btn_likes[1].getText()
        dislike = btn_likes[3].getText()
	watch_movie = li.find('span', {'class':'ico_viewer'})

	print(created_at, review_text, score, like, dislike, watch_movie and True or False, nickname)

test_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=119412&type=after'
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')
result = html.find('div', {'class':'score_total'}).find('strong').findChildren('em')[1].getText()
total_count = int(result.replace(',', ''))

for i in range(1, int(total_count / 10) + 1):
    url = test_url + '&page=' + str(i)
    get_data(url)
