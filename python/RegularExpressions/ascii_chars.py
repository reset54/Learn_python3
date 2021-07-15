import re


pattern_1 = r"(\D+\d)"
pattern_2 = r"(\W+\d)"
pattern_3 = r"(\S+\s)"
pattern_4 = r"(\D+\d)"

def test(p: str) -> None:
  print("\n      for " + p + "\n")
  match = re.match(p, "Hi 999!")
  if match:
    print("True,    Hi 999!")
  else:
    print("false,    Hi 999!")

  match = re.match(p, "1, 23, 456!")
  if match:
    print("True,    1, 23, 456!")
  else:
    print("false, '1, 23, 456!'")

  match = re.match(p, " ! $?")
  if match:
    print("True,     ! $?")
  else:
    print("false, ' ! $?'")

test(pattern_1)
test(pattern_2) 
test(pattern_3)
test(pattern_4)