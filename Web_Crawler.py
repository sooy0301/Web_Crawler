import requests
import warnings
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
import time

warnings.filterwarnings(action='ignore')

with open('pageList.txt', 'r') as f:
    data = f.read()
url = data.splitlines()

number = 1
index = 1
check = 1
noReply = 0

def func (url, time):

    global number
    global index
    global noReply
    global check
   
#     loginurl= 'https://www.ipmarket.or.kr/idearo/service/cmn/login/actionLogin.do'
    session = requests.session()
#     params = dict()
#     params['id'] = 'ID'
#     params['password'] = 'PW'
#     params['userSE'] = 'GNR1'
#     params['snsAuth'] = 'snsAuth2'

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36" }

#     res = session.post(loginurl, data = params,  headers=headers, verify=False)
    response = session.get(url, headers=headers, verify=False)
   
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
              
        names = soup.select_one('li')
        title = soup.select_one('#cmmtlist')  
       
        if names != None:     
            names_title = names.find('p', class_='tit')
            names_name = names.find('p', class_='name')

            title_time = title.find_all('span', class_='time')
            title_name = title.find_all('strong', class_='name')
            title_txt = title.find_all('p', class_='txt')
           
#            print(number, '. Checked : ', names_title.text, '-',names_name.text)
            number = number + 1
            if title_time != [] :
                for idx, tag in enumerate(title_time):
                    # and re.sub('[^a-zA-Zㄱ-힗]', '', title_name[idx].text) != '' :
#                     if tag.text == '2021.10.14' :
                    if tag.text[0:7] == '2021.10' :
                        print(index, '.──────────────────────────────────────────────')
                        print(url)   
                        print(names_title.text, '-',names_name.text)  
                        print(title_name[idx].text, '-', tag.text)
                        print(title_txt[idx].text)
                        #print(re.sub('[^a-zA-Zㄱ-힗]', '', title_name[idx].text))
                        print('----──────────────────────────────────────────────')
                        noReply = 1
                        index = index + 1
        else:
            print('페이지 없음 ─ ', url)
    else :
        print(response.status_code)
       
for address in url:
    func(address, 'null')
    time.sleep(1.5)
       
if noReply == 0: print('댓글 찾지 못함')
today = datetime.today().strftime("%Y.%m.%d")
print('──────────────────────  Fin  ───────────────────────')


# 배포이후 변한 점
#  1.댓글 번호 추가  2. 기업회원(알파벳 없는 id)의 댓글 제외 3. 댓글 없으면 없다고 함