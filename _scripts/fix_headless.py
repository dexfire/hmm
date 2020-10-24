# coding=utf8
import os

path = "../source/_posts"
os.chdir(path)
fs = [fn for fn in os.listdir(".") if fn.endswith(".md")]

for fn in fs:
    try:
        with open(fn, "r", encoding="utf8") as f:
            text = f.read()
            if not text.startswith("---"):
                text = "---\n---\n" + text
            else:
                text = None
    except UnicodeDecodeError as e:
        print("#! error while reading " + fn)
        print(e)
        try:
            with open(fn, "r", encoding="gbk") as f:
                text = f.read()
                if not text.startswith("---"):
                    text = "---\n---\n" + text

        except UnicodeDecodeError as e:
            print("##! error while reading " + fn)
            print(e)

    try:
        if text is not None:
            with open(fn, "w", encoding="utf8",) as f:
                f.write(text)
                f.close()
                print("Modified: " + fn)
    except Exception as e:
        print("#! error at " + fn)
        print(e)
