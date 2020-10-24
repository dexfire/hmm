# coding=utf8
import sys
import pyperclip

print(sys.argv)
s = '![](/img/' + p[p.rfind('\\')+1:len(p)] + ')'
pyperclip.copy(s)
# input('按任意键退出。')