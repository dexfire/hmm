# coding=utf8
import os
import re


def fmt(m: re.match):
	return "{% raw %}$a^{{a_1}^{{a_2}}}${% endraw %}"


path = "../source/_posts"
os.chdir(path)
fs = [fn for fn in os.listdir(".") if fn.endswith(".md")]

for fn in fs:
	try:
		with open(fn, "r", encoding="utf8") as f:
			text = f.read()
			text.index("/assets/images/")
			f.close()
	except UnicodeDecodeError as e:
		print("#! error while reading " + fn)
		print(e)
		try:
			with open(fn, "r", encoding="gbk") as f:
				text = f.read()
				text.index("/assets/images/")
				f.close()
		except UnicodeDecodeError as e:
			print("##! error while reading " + fn)
			print(e)
		except ValueError:
			text = None
			print("skiping file " + fn)
	except ValueError:
		text = None
		print("skiping file " + fn)

	try:
		if text is not None:
			text = re.sub(r"/assets/images/", "/img/", text)
			with open(fn, "w", encoding="utf8",) as f:
				f.write(text)
				f.close()
				print("Modified: " + fn)
	except Exception as e:
		print("#! error at " + fn)
		print(e)
