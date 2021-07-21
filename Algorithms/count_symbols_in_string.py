<<<<<<< HEAD
# взято из https://www.youtube.com/watch?v=QLhqYNsPIVo&ab_channel=%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0

# Наиболее часто встречающийся символ в строке
# Option 1 (for in for )
# O(N**2) - Time
# O(N) - Memory
# string = input() # type = str
string = "shgoioiwngv;ophvniewh vnoikkjeisdaf"# test

ans = "" # type = str
ans_count = 0 #anscnt
for i in range(len(string)):
    now_count = 0
    for j in range(len(string)):
        if string[i] == string[j]: # check equal
            now_count += 1
    if now_count > ans_count: # check more meeting symbol
        ans = string[i]
        ans_count = now_count
print(f"Option 1: {ans} for {string}")

# Option 2 (set O)
# O(N*K) - Time
# (N+K)≈O(N) - Memory
# string_2 = input() # type = str
string_2 = "shgoioiwngv;ophvniewh vnoikkjeisdaf"# test
ans = "" # type = str
ans_count = 0 
for now in set(string_2): # no identikal values in set
    now_count = 0
    for j in range(len(string_2)):
        if now == string_2[j]: # check equal
            now_count += 1
    if now_count > ans_count: # check more meeting symbol
        ans = now
        ans_count = now_count
print(f"Option 2: {ans} for {string_2}")

# Option 3 (dict)
# O(N) - Time
# O(K) - Memory (K<N)
#string_3 = input() # type = str
string_3 = "shgoioiwngv;ophvniewh vnoikkjeisdaf"# test
ans = "" # type = str
ans_count = 0 
dct = {}
for now in string_3: # no identikal values in set
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
    # print(dct[now])
for key in dct: 
    if dct[key] > ans_count: # check more meeting symbol
        ans_count = dct[key]
        ans = key
print(f"Option 3: {ans} for {string_3}")
=======
# взято из https://www.youtube.com/watch?v=QLhqYNsPIVo&ab_channel=%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0

# Наиболее часто встречающийся символ в строке
# Option 1 (for in for )
# O(N**2) - Time
# O(N) - Memory
# string = input() # type = str
string = "shgoioiwngv;ophvniewh vnoikkjeisdaf"# test

ans = "" # type = str
ans_count = 0 #anscnt
for i in range(len(string)):
    now_count = 0
    for j in range(len(string)):
        if string[i] == string[j]: # check equal
            now_count += 1
    if now_count > ans_count: # check more meeting symbol
        ans = string[i]
        ans_count = now_count
print(f"Option 1: '{ans}' for string '{string}'")

# Option 2 (set O)
# O(N*K) - Time
# (N+K)≈O(N) - Memory
# string_2 = input() # type = str
string_2 = "shgoioiwngv;ophvniewh vnoikkjeisdaf"# test
ans = "" # type = str
ans_count = 0 
for now in set(string_2): # no identikal values in set
    now_count = 0
    for j in range(len(string_2)):
        if now == string_2[j]: # check equal
            now_count += 1
    if now_count > ans_count: # check more meeting symbol
        ans = now
        ans_count = now_count
print(f"Option 2: '{ans}' for string '{string_2}'")

# Option 3 (dict)
# O(N) - Time
# O(K) - Memory (K<N)
#string_3 = input() # type = str
string_3 = "shgoioiwngv;ophvniewh vnoikkjeisdaf"# test
ans = "" # type = str
ans_count = 0 
dct = {}
for now in string_3:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
    # print(dct[now])
for key in dct: 
    if dct[key] > ans_count: # check more meeting symbol
        ans_count = dct[key]
        ans = key
print(f"Option 3: '{ans}' for string '{string_3}'")
>>>>>>> refs/remotes/origin/readme
