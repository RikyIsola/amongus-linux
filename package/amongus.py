from bs4 import BeautifulSoup
from requests import get
from argparse import ArgumentParser

parser=ArgumentParser()
parser.add_argument('file',type=str,help='Where to put the file')
args=parser.parse_args()
soup=BeautifulSoup(get('https://apkpure.com/among-us/com.innersloth.spacemafia/download?from=details').content,
                   features='html.parser')
with open(args.file,'wb') as f:
    f.write(get(soup.find('a',{'id':'download_link'})['href']).content)
