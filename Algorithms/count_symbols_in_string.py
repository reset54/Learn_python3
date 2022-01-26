# взято из https://www.youtube.com/watch?v=QLhqYNsPIVo&ab_channel=%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0
# Наиболее часто встречающийся символ в строке


def find_sym_in_str_1(input_str: str) -> str:
    """
    Option 1 (for in for)
    O(N**2) - Time
    O(N) - Memory
    """
    ans = "" # type = str
    ans_count = 0 #anscnt
    for i in range(len(input_str)):
        now_count = 0
        for j in range(len(input_str)):
            if input_str[i] == input_str[j]:          # check equal
                now_count += 1
        if now_count > ans_count:               # check more meeting symbol
            ans = input_str[i]
            ans_count = now_count
    return(f"Option 2:\n Наиболее часто встречающийся символ в строке: {ans}, для строки:\n {input_str}")


def find_sym_in_str_2(input_str: str) -> str:
    """
    Option 2 (set O)
    O(N*K) - Time
    (N+K)≈O(N) - Memory
    """
    ans = ""
    ans_count = 0 
    for now in set(input_str):           # no identikal values in set
        now_count = 0
        for j in range(len(input_str)):
            if now == input_str[j]:      # check equal
                now_count += 1
        if now_count > ans_count:           # check more meeting symbol
            ans = now
            ans_count = now_count
    return(f"Option 2:\n Наиболее часто встречающийся символ в строке: {ans}, для строки:\n {input_str}")


def find_sym_in_str_3(input_str: str) -> str:
    """
    Option 3 (dict)
    O(N) - Time
    O(K) - Memory (K<N)
    """
    ans = ""
    ans_count = 0 
    dct = {}
    for now in input_str: # no identikal values in set
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
        # print(dct[now])
    for key in dct: 
        if dct[key] > ans_count: # check more meeting symbol
            ans_count = dct[key]
            ans = key
    return(f"Option 3:\n Наиболее часто встречающийся символ в строке: {ans}, для строки:\n {input_str}")


# test
def test(input_str):
    print(f"\nTestCase 1 (for in for):\n {find_sym_in_str_1(input_str)}")
    print(f"\nTestCase 2 (set O):\n {find_sym_in_str_2(input_str)}")
    print(f"\nTestCase 3 (dict):\n {find_sym_in_str_3(input_str)}")


# run_test
our_string = "shgoioiwngv;ophvniewh vnoikkjeisdaf"
test(our_string)
test(input())
