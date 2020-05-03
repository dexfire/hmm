# coding=utf8
import os
import re


def fmt(m):
	if len(m.groups())==3:
		t = str(m.group(2))
		print(" <- tags: " + t)
		# m2 = re.match("([^\s]+?),()")
		li = t.split(", ")
		str1 = "  - " + "\n  - ".join(li)
		str2 = m.group(1) + "\n" + str1 + "\n" + m.group(3)
		print(" -> result: " + str2)
		return str2
	else:
		print("error-matching...")
		return m.group(0)
path = "../source/_posts"
os.chdir(path)
fs = [fn for fn in os.listdir(".") if fn.endswith(".md")]
pattern = r"(---\n.+?tags:)\s\[(.+?)\]\n(.+?\n---.*)"

for fn in fs:
	try:
		with open(fn, "r", encoding="utf8") as f:
			text = f.read()
			s = re.search(pattern, text, flags = re.DOTALL + re.MULTILINE)
			f.close()
			if s is None:
				print("skiping file " + fn)
				continue
	except UnicodeDecodeError as e:
		print("#! error while reading " + fn)
		print(e)
		try:
			with open(fn, "r", encoding="gbk") as f:
				text = f.read()
				s = re.search(pattern, text, flags = re.DOTALL + re.MULTILINE)
				f.close()
				if s is None:
					print("skiping file " + fn)
					continue
		except UnicodeDecodeError as e:
			print("##! error while reading " + fn)
			print(e)

	try:
		if s is not None:
			text = re.sub(pattern, fmt, text, flags = re.DOTALL + re.MULTILINE)
			with open(fn, "w", encoding="utf8",) as f:
				f.write(text)
				f.close()
				print("Modified: " + fn)
	except Exception as e:
		print("#! error at " + fn)
		print(e)
