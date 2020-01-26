import requests
import re
from bs4 import BeautifulSoup
import boto3

URL = 'https://en.wikipedia.org/wiki/India'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
soup1 = str(soup)
#print(soup1)

p_tags = soup.findAll('p')


soup_string = str(p_tags)

clean = re.compile('<.*?>,\W')

clean = re.compile('\W')

clean_data = re.sub(clean,'',soup_string)

#print(clean_data)


s3 = boto3.resource('s3')
object = s3.Object('unstructproject', 'unstruct.txt')
object.put(Body=clean_data)


s31 = boto3.resource('s3')
object1 = s31.Object('semistrctproject', 'semistruct.txt')
object1.put(Body=soup1)

