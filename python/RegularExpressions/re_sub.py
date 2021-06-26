import re
# print(help(re.sub))

oldstring = "My name is David. Hi David."
print (oldstring)
pattern = r"David"

# по сути (replace) замена паттерна(pattern-шаблон) нашей строкой, делаем новую строку
newstring = re.sub(
                pattern, 
                "Amy",                       
                oldstring
)
print(f"{newstring} \n\n")

