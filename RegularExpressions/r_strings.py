import re

pattern = r"х.й"

if re.match(pattern, "хей"):
    print("Match 1")
else:
    print("NO Match_1")
if re.match(pattern, "хай"):
    print("Match 2")
else:
    print("NO Match_2")
if re.match(pattern, "хирльирьтий"):
    print("Match 3")
else:
    print("NO Match_3")
if re.match(pattern, "хй"):
    print("Match 4")
else:
    print("NO Match_4")
if re.match(pattern, ""):
    print("Match 5")
else:
    print("NO Match_5")

print('        "^" - symbol start string')
print('        "$" - symbol end string') 


pattern_2 = r"^y...o$"
if re.match(pattern_2, "yello"):
    print("Match_1")
else:
    print("NO Match_1")
if re.match(pattern_2, "yahoo"):
    print("Match_2")
else:
    print("NO Match_2")
if re.match(pattern_2, "yellow"):
    print("Match_3")
else:
    print("NO Match_3")
if re.match(pattern_2, "yrgcn"):
    print("Match_4")
else:
    print("NO Match_4")