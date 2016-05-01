#encoding utf-8
import requests
from bs4 import BeautifulSoup
import types

def get_pusher(url,rs,target):
  #intialzie list
  pushlist=[]

  res=rs.get(url)
  code=BeautifulSoup(res.text)

  print '     Search :%s'%url
  for item in code.find_all('div',attrs={'class':'push'}):
    pusher=item.find('span','f3 hl push-userid')

    if pusher!=None and pusher.text==target:
      content=item.find('span','f3 push-content')
      tag=item.find('span','f1 hl push-tag')
      datetime=item.find('span','push-ipdatetime')
      if tag==None:
        tag=item.find('span','hl push-tag')

      print '        ',tag.text,pusher.text,content.text,datetime.text
      pushlist.append(tag.text+pusher.text+content.text+datetime.text)

  #add url to end of pushlist
  if len(pushlist)!=0:
    pushlist[len(pushlist)-1]+='\n     Url:%s\n\n'%url
  return pushlist


