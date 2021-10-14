import sys
import re
from collections import Counter


# many strings enter in console (many strings input())
random_text = sys.stdin.readlines() # -> list
print("10 самых часто встречающихся слов в этом тексте:\n") # for words containing more 2 symbols


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
        if len(key) < 3:                  # words > 3 symbols
            del words[key]
    return(words)                         # -> <class 'collections.Counter'>


def sort_alphabet_counter_keys(counter):  
    # result = counter.most_common(10)
    # result = sorted(result.items())
    sort_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0])) 
    # -> list [("key", value),]
    top_ten = sort_counter[:10]
    return top_ten


def printByLine(tuples):
    print('\n'.join(''.join(map(str, t)) for t in tuples))

result = find_words_in_text(edit_text(random_text))
# result = printByLine(result)

result = sort_alphabet_counter_keys(result)

# print(f"{result}\n\n\n")
for i in result:
    key, value = i 
    print(f"{key}: {value}")
    if i == 10:
        break
