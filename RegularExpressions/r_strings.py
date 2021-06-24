import re

pattern = r"х.й"

def test_matching(pattern):
    """check match with pattern"""
    if re.match(pattern, "хей"):
        print("YES Match test 1")
    else:
        print("NO Match test 1")
    if re.match(pattern, "хай"):
        print("YES Match test 2")
    else:
        print("NO Match test 2")
    if re.match(pattern, "хирльирьтий"):
        print("YES Match test 3")
    else:
        print("NO Match test 3")
    if re.match(pattern, "хй"):
        print("YES Match test 4")
    else:
        print("NO Match test 4")
    if re.match(pattern, ""):
        print("YES Match test 5")
    else:
        print("NO Match test 5")

print('        "^" - symbol start string')
print('        "$" - symbol end string') 


pattern_2 = r"^y...o$"

if re.match(pattern_2, "yello"):
    print("YES Match test 1")
else:
    print("NO Match test 1")
if re.match(pattern_2, "yahoo"):
    print("YES Match test 2")
else:
    print("NO Match test 2")
if re.match(pattern_2, "yellow"):
    print("YES Match test 3")
else:
    print("NO Match test 3")
if re.match(pattern_2, "yrgcn"):
    print("YES Match test 4")
else:
    print("NO Match test 4")