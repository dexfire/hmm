# coding=utf8
import sys
import pyperclip

try:
	#print(sys.argv)
	p=str(sys.argv[1])
	s = '![](/img/' + p[p.rfind('\\')+1:len(p)] + ')'
	#print(s)
	pyperclip.copy(s)
	# input('按任意键退出。')
except:
	pass