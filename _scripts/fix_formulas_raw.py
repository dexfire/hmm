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
            if text.index("$") == -1:
                text = None
            f.close()
    except UnicodeDecodeError as e:
        print("#! error while reading " + fn)
        print(e)
        try:
            with open(fn, "r", encoding="gbk") as f:
                text = f.read()
                if text.index("$") == -1:
                    text = None
                f.close()
        except UnicodeDecodeError as e:
            print("##! error while reading " + fn)
            print(e)
        except ValueError:
            pass
    except ValueError:
        pass

    try:
        if text is not None:
            text = re.sub(
                r"(\$\$.+?\$\$)", "\n{% raw %}\n\1\n${% endraw %}\n", text)
            text = re.sub(
                r"(\$.+?\$)", "\n{% raw %}\n\1\n${% endraw %}\n", text)
            with open(fn, "w", encoding="utf8",) as f:
                f.write(text)
                f.close()
                print("Modified: " + fn)
    except Exception as e:
        print("#! error at " + fn)
        print(e)
