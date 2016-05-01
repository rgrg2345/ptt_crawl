#encoding utf-8
from bs4 import BeautifulSoup
import requests
import sys
import ptt_over18

def get_essayinfo(*arg):

  #test_url='https://www.ptt.cc/bbs/Grad-ProbAsk/M.1460432922.A.E6E.html'
  #print '%s \n %s\n ' %(authorlist[i],urlist[i])

  #initalize list
  metalist=[]
  essaylist=[]

  #initial setting
  url=arg[0]

  if len(arg)==2:
    rs = arg[1]
  else:
    rs=requests.session()
  res=rs.get(url)
  code=BeautifulSoup(res.text)

  #for item in code.select('.article-metaline'): #will get 3 item type[list]
                                                #0:author
                                                #1:title
                                                #2:date
  #  print item
  #  print item.select('.article-meat-value')
    #for i in range(len(item)):
      #if i % 2 ==1:
        #metalist.append(item.text)
        #print metalist[len(metalist)-1]

  """meta list   0 Author
                 2 Title
                 4 Date
  """

  #Get span text
  for item in code.find_all('div',attrs={'class':'article-metaline'}):
    metalist.append(item.find('span','article-meta-value').text)

  essaylist.append(metalist)

  #essay content
  essaylist.append(code.select('#main-container')[0].text)

  #essay html
  essaylist.append(code.select('#main-container')[0])

  return essaylist


if __name__=='__main__':
  get_essayinfo('')
