import re
"""re.search meta chars"""
#  only not  big, nums
pattern = r"[^A-Z ^0-9]"

if re.search(pattern, "this is all quiet"):
    print("Match 1 small chars")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2 small, big, nums")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3 only big chars")

if re.search(pattern, "ABC123"):
    print("Match 4 big, nums")

if re.search(pattern, "ThisIsAllShooting"):
    print("Match 5")
