#encoding utf-8
from bs4 import BeautifulSoup
import requests
import re
from sys import argv
from time import sleep

import ptt_get_essay
import ptt_dl
import ptt_print
import ptt_over18
import ptt_get_pusher


#for test
from types import *
loop=100

#tag='Grad-ProbAsk'
#tag='joke'
#tag='graduate'
tag ='Gossiping'
#tag='Baseball'
def get_essay_list(*arg):

  #initalize
  indexUrl = 'https://www.ptt.cc/bbs/%s/index.html'%tag
  #essaylist=[]
  #pushlist=[]
  tarlist=[]

  #cond: true for continue search
  cond=True

  #test counter
  counter=0

  #res=ptt_over18.check_over18(indexUrl)

  if len(arg)!=0:
    target=arg[0]
    mode=arg[1]

  #rs=ptt_over18.check_over18(indexUrl)

  while cond == True:

    #initial lists
    urlist=[]

    print 'Connect to ptt.cc ..'
    print 'Loading Url :%s\n'%indexUrl

    rs=ptt_over18.check_over18(indexUrl)
    res = rs.get(indexUrl)
    code = BeautifulSoup(res.text)


    for item in code.select('.r-ent'):

      #Get essay author
      author=item.select('.author')[0].text
      #authorlist.append(author)

      #mode 2  get author essay
      if mode==2 and author!=target:
        continue

      #Using regular expression to get url
      m=re.search('/bbs/%s/.+(?:html)'%tag,str(item.select('.title')[0]))
      if m :
        url='https://www.ptt.cc'+m.group()
        urlist.append(url)

        if mode == 1:
          tarlist.extend(ptt_get_pusher.get_pusher(url,rs,target))
        else:
          essayinfo=ptt_get_essay.get_essayinfo(url,rs)
          tarlist.append(essayinfo)

        #ptt_print_essay.print_essay(essayinfo)
        #find wait a moment
        #sleep(1)



    bdurlist=get_board_url(code)

    #retry to get board url
    #cause of 503 nginx
    if len(bdurlist)==0:
      print code.text
      sleep(0.5)
      continue

    #url is the earliest one
    if bdurlist[0]==indexUrl:
      cond=False
    else:
    #get earlier url
      indexUrl=bdurlist[1]

    counter+=1
    if counter>loop:
      cond=False

    #prevent for banning by server, wait a while
    #sleep(1)

  print 'Total find %d objects'%len(tarlist)
  if mode ==1:
    ptt_print.print_push(tarlist)
    ptt_dl.dl_push(tarlist,target)
  else:
    print_all_essay(tarlist)

def get_board_url(code):
  #Get earliest url
  #    prev url
  #    next url
  #    lateist url
  for item in code.select('.btn-group.btn-group-paging'):
    mlist=re.findall('/bbs/%s/index.+(?:html)'%tag,str(item))
    if mlist:
      for i in range(len(mlist)):
        mlist[i]='https://www.ptt.cc'+mlist[i]
        #print mlist[i]
      return mlist
  return []

def print_all_essay(essaylist):
  if len(essaylist)!=0:
    for item in essaylist:
      ptt_print.print_essayinfo(item)

if __name__=='__main__':
  #get_essay_list('amge1524',1)
  #get_essay_list('jerry031181',1)
  get_essay_list('prosperous',1)
  #get_essay_list('obov',1)
  #get_essay_list('eagle1128',1)
  #get_essay_list('xxtuoo',1)
  #get_essay_list()
