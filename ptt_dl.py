#encoding utf-8
import ptt_get_essay
import copy2file

def dl_essay(essayinfo):
  #initial lists
  #urlist,meta_list,essay=ptt_get_essay.get_essay()

  copy2file.copy('%s_%s'%(essayinfo[1][1],essayinfo[1][0]),essayinfo[0]+essayinfo[2],1)

def dl_push(pushlist,target):
  copy2file.copy(target,list2str(pushlist),2)
def list2str(li):
  string=''
  for item in li:
    string+=item
  return string

if __name__=='__main__':
  dl_essay()
