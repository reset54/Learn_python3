import re


pattern_1 = r"(pul|req|fer)"
pattern_2 = r"(pul|req|fer)\1"
pattern_3 = r"(pu|xyz| )"
pattern_4 = r"(pu|xyz| )\1"

def test(p):
  
  print("    pattern = " + p + "\n")
  if re.match(p, "pullrequests"):
    print(f"True, {: > 10}.format("pullrequests"))
  else:
    print("False, pullrequests")
  
  if re.match(p, "xyzxyz"):
    print("True,    xyzxyz")
  else:
    print("False, xyzxyz")

  if re.match(p, "ferabc"):
    print("True,    ferabc")
  else:
    print("False, ferabc")
  
  if re.match(p, "xyz xyz"): 
    print("True,    xyz xyz")
  else:
    print("False, xyz xyz")
      
  if re.match(p, "abcxyz"): 
    print("True,    abcxyz")
  else:
    print("False, abcxyz")
    
  if re.match(p, "xyzabc"): 
    print("True,    xyzabc")
  else:
    print("False, xyzabc")
    
  if re.match(p, "ferrum"): 
    print("True,    ferrum")
  else:
    print("False, ferrum")
    
print()
test(pattern_1)
print()
test(pattern_2)
print()
test(pattern_3)
print()
test(pattern_4)
print()