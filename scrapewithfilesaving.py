from bs4 import BeautifulSoup
import requests
import time

print('Put some skill which you are unfamiliar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  ##scrape all the li tags and with class name = 'clearfix job-bx wht-shd-bx
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')  ## with no whitespace in the front
            skill = job.find('span', class_='srp-skills').text.replace(" ", '')
            more_info = job.h2.a['href']  ## go to subheader a of h2 of i and call the href attribute of a
            if unfamiliar_skill not in skill:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name = {company_name.strip()}\n")
                    f.write(f"Required skills = {skill.strip()}\n")
                    f.write(f"More Info = {more_info}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting for {time_wait} minute(s)...')
        time.sleep(time_wait * 60)
