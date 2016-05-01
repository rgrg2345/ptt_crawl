#encoding utf-8
import requests
from bs4 import BeautifulSoup

def check_over18(url):

  res = requests.get(url)
  code = BeautifulSoup(res.text)

  if len(code.select('.over18-notice'))!=0:
    payload={
        'from':url[18:],
        'yes':'yes'
        }
    rs=requests.session()
    res=rs.post('https://www.ptt.cc/ask/over18',data=payload)
    res=rs.get(url)
    #code=BeautifulSoup(res2.text)
    return rs
  else:
    return requests.session()
  #print code
  #for item in code.select('.r-ent'):
  #  print item.select('.title')[0]

def main():
  code = check_over18('https://www.ptt.cc/bbs/gossiping/index.html')
  for item in code.select('.r-ent'):
    print item.select('.title')[0],"\n\n"


if __name__=='__main__':
  main()

