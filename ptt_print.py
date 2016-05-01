#encoding utf-8
from types import *

def print_essayinfo(essaylist):
  if len(essaylist)!=0:
    for item in essaylist:
      if type(item)==ListType:
        for li in item:
          print li
      else:
        print item

def print_essay(essaylist):
  if len(essaylist)!=0:
    print essaylist[2]

def print_push(pushlist):
  if len(pushlist)!=0:
    for item in pushlist:
      print item
