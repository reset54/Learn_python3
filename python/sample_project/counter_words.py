import sys
import re
from collections import Counter

# many strings enter in console (many strings input())
# random_text = sys.stdin.readlines() # -> list
random_text = """
Ты жива еще, моя старушка?
Жив и я. Привет тебе, привет!
Пусть струится над твоей избушкой
Тот вечерний несказанный свет.

Пишут мне, что ты, тая тревогу,
Загрустила шибко обо мне,
Что ты часто ходишь на дорогу
В старомодном ветхом шушуне.

И тебе в вечернем синем мраке
Часто видится одно и то ж:
Будто кто-то мне в кабацкой драке
Саданул под сердце финский нож.

Ничего, родная! Успокойся.
Это только тягостная бредь.
Не такой уж горький я пропойца,
Чтоб, тебя не видя, умереть.

Я по-прежнему такой же нежный
И мечтаю только лишь о том,
Чтоб скорее от тоски мятежной
Воротиться в низенький наш дом.

Я вернусь, когда раскинет ветви
По-весеннему наш белый сад.
Только ты меня уж на рассвете
Не буди, как восемь лет назад.

Не буди того, что отмечталось,
Не волнуй того, что не сбылось, —
Слишком раннюю утрату и усталость
Испытать мне в жизни привелось.

И молиться не учи меня. Не надо!
К старому возврата больше нет.
Ты одна мне помощь и отрада,
Ты одна мне несказанный свет.

Так забудь же про свою тревогу,
Не грусти так шибко обо мне.
Не ходи так часто на дорогу
В старомодном ветхом шушуне.
"""

print("10 самых часто встречающихся слов в этом тексте:\n") # for words containing more 3 symbols

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
        if len(key) < 3:                    # words > 3 symbols
            del words[key]
    return(words)                          # -> <class 'collections.Counter'>

def sort_alphabet_counter_keys(counter):  # -> list [("key", value),]
    #result = counter
    result = sorted(counter.items())
    #print(type(result))
    return result

def printByLine(tuples):
    print('\n'.join(''.join(map(str, t)) for t in tuples))

result = find_words_in_text(edit_text(random_text))
# result = printByLine(result)

#result = sort_alphabet_counter_keys(result)

print(result)
for i in result:
    key, value = i 
    print(f"{key}: {value}")
    if i == 10:
        break
# print(result)