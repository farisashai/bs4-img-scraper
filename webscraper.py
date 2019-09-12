from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests

query = input('Search Query: ')
url = 'https://www.google.com/search?tbm=isch&q={0}'.format(query)
response = requests.get(url)
content = BeautifulSoup(response.content,'html.parser')

for num,img in enumerate(content.findAll('img')):
    string = img['src'];
    picture = requests.get(string)
    Image.open(BytesIO(picture.content)).convert('RGB').save('results/{0}.jpg'.format(num))
    print(num,string)
