import requests
from bs4 import BeautifulSoup
from pprint import pprint

url=requests.get('https://news.ycombinator.com/news')
url2=requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(url.text, 'html.parser')
soup2 = BeautifulSoup(url2.text, 'html.parser')


links=soup.select('.titlelink')
subtext=soup.select('.subtext')
links2=soup2.select('.titlelink')
subtext2=soup2.select('.subtext')

mega_links=links+links2
mega_subtext=subtext+subtext2



def custom_hackernews(mega_links,mega_subtext):
    hackernews=[]

    for index,item in enumerate(links):
        title=item.getText()
        link=item.get('href')
        votes=mega_subtext[index].select('.score')
        if len(votes):
            points=int(votes[0].getText().replace(' points',''))
            if points>99:
                hackernews.append({'title':title, 'links':link, 'userpoints':points})

    return hackernews


def sorted_custom_hackernews(hackernewslist):
    return sorted(hackernewslist,key= lambda k:k['userpoints'],reverse=True)



#pprint(custom_hackernews(mega_links,mega_subtext))


hnws=custom_hackernews(mega_links,mega_subtext)
pprint(sorted_custom_hackernews(hnws))

