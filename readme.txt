Using ptt_get_url_list to get essayurl

	essayurl 
		type:list
		store:
			essayinfo
All essay store in essayinfo

	essayinfo 
		type:list
		store:
			0:essay url
			1:meta info
				type:list
				store:
					0:author
					1:essay title
					2:date
			2:essay(plain text)
			3:essay(html)

Functions
	ptt_get_url_list.py
		get_essay_list(target,mode)

	ptt_get_essay.py
		get_essayinfo(url,?rs)
		return essaylist

	ptt_dl.py
		dl_essay(essayinfo)no return
		dl_push(pushlist,target)no return
		list2str(list)return string
		
	ptt_over18(url)
		return requests.session()

	ptt_print.py
		print_essayinfo(essaylist)no return
		print_essay(essaylist)no return
		print_push(pushlist)no return
	copy2file.py
		copy(filename,text,mode)
			mode 	0:no overwrite
				1:overwrite
				2:append
	

