# https://youtu.be/8cMMO8fks-k
# https://youtu.be/vn6bV6BYm7w
from typing import Generator

Number = 10
input_list_1 = [43, 65, 32]

def gen_function(input_list):
    s = 1
    for i in input_list:
        yield i
        print(s)
        s = s + 1


def factorial(num: int) -> list:
    pr = 1
    list_1 = []
    for i in range (1, num+1):
        pr = pr * i
        list_1.append(pr)
    return list_1


def factorial_generate(num: int) -> Generator[int, None, None]:
    pr = 1
    for i in range (1, num+1):
        pr = pr * i
        yield pr


# tests
def test_steps_generate(gen):
    i = 1
    while(gen):
        try:
	    print(f"Step generate {i} out: {next(gen)}")
	    i += 1
	except StopIteration:
	    print("Итерации далее невозможны, iterable больше не содержит элементов\n\n")
	    break


# run tests
variable_1 = gen_function(input_list_1)
test_steps_generate(variable_1)


variable_2 = factorial_generate(Number)
test_steps_generate(variable_2)

list_variable = [x for x in input_list_1]
print(f"[x for x in input_list_1] = {list_variable}\n\n")

for i in factorial(10):
    print(i, end = "-,-")
print(factorial(15), end = "\n\n")
