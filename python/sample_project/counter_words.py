import sys
import re
from collections import Counter
import pprint


# many strings enter in console (many strings input())
random_text = sys.stdin.readlines() # -> list

print("10 самых часто встречающихся слов в этом тексте:") # for words containing more 3 symbols

def edit_text(text):
    forbidden = ('.','?','!',':',';','-','—',',')
    new_text = "".join(symbol for symbol in text if symbol not in forbidden)
    new_text = new_text.lower()
    # new_text = "".join(symbol for symbol in random_text if symbol.isalnum()) # оставить только буквы и цифры
    return new_text

def find_words_in_text(text):
    words = re.findall(r'\w+', text)
    words = Counter(words)
    # print(words)
    for key in list(words):
        # print(len(key))
        if len(key) < 3:
            del words[key]
    print(words) # list

def countsSortedAlphabetically(counter, **kw):
    return sorted(counter.items(), **kw)

def printByLine(tuples):
    print('\n'.join(' '.join(map(str, t)) for t in tuples))



result = find_words_in_text(edit_text(random_text))

#result = countsSortedAlphabetically(result, reverse=True)
#result = printByLine(result)
# print(pprint.pformat(result))
#for i in range(10):
#    print(len(result[i][0]))
#    if len(result[i][0]) > 3:
result = result.most_common(10)
#        print(f"{result[i][0]} : {result[i][1]}")

#res = [i for i in range(10) if len(result[i][0]) > 3]
print(result)