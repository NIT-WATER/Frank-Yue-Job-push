import requests
from bs4 import BeautifulSoup as bs
from common.Struct import *
from datetime import datetime

def crawl_information(user_info, company_info, config):
    return_string = ''
    split_string = '********************'
    min_days = 3 
    for key_word in user_info.key_words:
        #url = "https://www.aetnacareers.com/search-jobs/SQL"
        url = company_info.url + '/' + config['key_word']
        print(url)
        strclass = "ant-table-row ant-table-row-level-0"
        hds = {
            'user-agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

        r = requests.get(url, headers=hds)
        soup = bs(r.text, 'html.parser')
        res = soup.findAll('li')
        #Jobid = []
        Jobname = []
        Jobdate = []
        Jobcity = []
        # print(res)
        for i in res:
            i = i.find('a')
            if i and i.get('data-job-id'):
                #Jobid.append(i.get('data-job-id'))
                Jobname.append(i.find('h2').text)
                city = i.find(name='span', attrs={"class": "job-location-search"}).text
                city = city.replace('\n', '').replace('\r', '')
                city = city.strip()
                Jobcity.append(city)
                Jobdate.append(i.find(name='span', attrs={"class": "job-date-posted"}).text)

        for i in range(len(Jobname)):
            msg_str = 'Job name: ' + Jobname[i] + '  Job city: ' + Jobcity[i] + ' Job post time: ' + Jobdate[i] + '\n'
            time_list = Jobdate[i].split('/')
            year = time_list[2]
            month = time_list[0]
            day = time_list[1]
            last_time = datetime(int(year), int(month), int(day))

            year = datetime.now().year
            month = datetime.now().month
            day = datetime.now().day

            now_time = datetime(year, month, day)
            cha_time = now_time - last_time
            if  cha_time.days <= min_days:
              return_string += (split_string + msg_str)

    if return_string == '':
      return "No new Job"
    return 'Here is the new Job\n' + return_string
